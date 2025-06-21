# Minecraft Auto Clicker

A simple Python auto clicker designed specifically for Minecraft weapons.  
Supports different weapon cooldown timings and toggleable left/right click, all configurable via an easy GUI.

---

## Requirements

- Python 3.8 or higher  
- [pyautogui](https://pypi.org/project/PyAutoGUI/)  
- [keyboard](https://pypi.org/project/keyboard/)  
- [rich](https://pypi.org/project/rich/)  
- Tkinter (usually included with Python on Windows and macOS)

---

## Installation

1. Clone this repository or download the source code.

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the auto clicker script:
```
python click_gui.py
```

## How To Use

    Select your weapon:
    Choose the Minecraft weapon you want to simulate from the dropdown menu. This sets the click delay according to that weapon's cooldown.

    Set your toggle key:
    Enter the key you want to use to start/stop the auto clicker, then click the "Set Keybind" button.

    Choose click button:
    Click the left or right click button to select which mouse button to auto-click.

    Toggle clicking:
    Press your chosen key to start or stop automatic clicking.
