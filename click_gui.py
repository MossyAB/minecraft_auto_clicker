import tkinter as tk
from tkinter import ttk, scrolledtext
import pyautogui
import keyboard
import threading
import time

WEAPON_COOLDOWNS = {
    "Netherite Sword": 0.625,
    "Diamond Sword": 0.625,
    "Iron Sword": 0.625,
    "Stone Sword": 0.625,
    "Wooden Sword": 0.625,
    "Trident": 0.909,
    "Netherite Axe": 1.0,
    "Diamond Axe": 1.0,
    "Iron Axe": 1.111,
    "Stone Axe": 1.25,
    "Wooden/Gold Axe": 1.0,
    "Pickaxe": 0.833,
    "Shovel": 1.0,
    "Hoe (Netherite/Diamond)": 0.25,
    "Hoe (Iron)": 0.333,
    "Hoe (Stone)": 0.5,
    "Hoe (Wood/Gold)": 1.0,
    "Fist / No weapon": 0.25,
}

Clicking = False
SelectedKey = ']'
SelectedDelay = 0.625
MouseButton = 'left'

# ---------- Auto Clicker Thread ----------
def click_loop():
    global Clicking, SelectedDelay
    while True:
        if Clicking:
            pyautogui.click(button=MouseButton)
            time.sleep(SelectedDelay if MouseButton == 'left' else 0.05)
        else:
            time.sleep(0.1)

# ---------- Key Toggle Thread ----------
def toggle_listener():
    global Clicking, SelectedKey
    while True:
        if keyboard.is_pressed(SelectedKey):
            Clicking = not Clicking
            if Clicking:
                log_to_console(f"Started clicking with key '{SelectedKey}'")
            else:
                log_to_console(f"Stopped clicking with key '{SelectedKey}'")
            while keyboard.is_pressed(SelectedKey):
                time.sleep(0.1)
        time.sleep(0.05)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Minecraft Auto Clicker")

frame = ttk.Frame(root, padding=20)
frame.pack()

# Weapon Dropdown
ttk.Label(frame, text="Select Weapon:").grid(row=0, column=0, sticky="w")
weapon_var = tk.StringVar(value="Netherite Sword")
weapon_menu = ttk.Combobox(frame, textvariable=weapon_var, values=list(WEAPON_COOLDOWNS.keys()), state="readonly", width=23)
weapon_menu.grid(row=0, column=1)
weapon_menu.bind("<<ComboboxSelected>>", lambda e: update_weapon())

# Keybind Entry
ttk.Label(frame, text="Change Keybind:").grid(row=1, column=0, sticky="w")
keybind_entry = ttk.Entry(frame)
keybind_entry.grid(row=1, column=1)
key_button = ttk.Button(frame, text="Set Keybind", command=lambda: update_keybind())
key_button.grid(row=1, column=2, padx=5)

key_label = ttk.Label(frame, text=f"Current Keybind: '{SelectedKey}'")
key_label.grid(row=2, column=0, columnspan=3, pady=10)

# Click Type Buttons
click_type_frame = ttk.Frame(frame)
click_type_frame.grid(row=3, column=0, columnspan=3, pady=5)

left_button = tk.Button(click_type_frame, text="Left Click", width=12, command=lambda: update_click_type("left"))
right_button = tk.Button(click_type_frame, text="Right Click", width=12, command=lambda: update_click_type("right"))

left_button.grid(row=0, column=0, padx=(0, 10))
right_button.grid(row=0, column=1)

ttk.Label(frame, text="Press the key to toggle clicking.").grid(row=4, column=0, columnspan=3, pady=5)

# ---------- Console Output ----------
console_output = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=6, state='disabled')
console_output.grid(row=5, column=0, columnspan=3, pady=(10, 0))

# ---------- GUI Functions ----------

# Add tags for colored text
console_output.tag_config("green", foreground="lime green")
console_output.tag_config("red", foreground="red")
console_output.tag_config("blue", foreground="blue")

def update_weapon():
    global SelectedDelay
    Weapon = weapon_var.get()
    SelectedDelay = WEAPON_COOLDOWNS.get(Weapon, 0.625)

def update_keybind():
    global SelectedKey
    new_key = keybind_entry.get().strip()
    if new_key:
        SelectedKey = new_key
        key_label.config(text=f"Current Keybind: '{SelectedKey}'")
        log_to_console(f"Updated keybind to '{SelectedKey}'")

def update_click_type(button):
    global MouseButton
    if button == "left":
        MouseButton = "left"
        left_button.configure(bg="#d9d9d9")
        right_button.configure(bg="#f0f0f0")
    elif button == "right":
        MouseButton = "right"
        right_button.configure(bg="#d9d9d9")
        left_button.configure(bg="#f0f0f0")
    log_to_console(f"Set mouse button to {button} click.")

def log_to_console(message):
    console_output.configure(state='normal')

    if "Started clicking" in message:
        tag = "green"
    elif "Stopped clicking" in message:
        tag = "red"
    else:
        tag = "blue"
    console_output.insert(tk.END, message + "\n", tag)
    console_output.configure(state='disabled')
    console_output.yview(tk.END)


# Now safe to call update_click_type
update_click_type("left")

# ---------- Start Threads ----------
threading.Thread(target=click_loop, daemon=True).start()
threading.Thread(target=toggle_listener, daemon=True).start()

# ---------- Run GUI ----------
root.mainloop()
