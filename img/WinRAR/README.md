# WinRAR Uninstall Automator

This script automates the uninstallation of WinRAR on a Windows machine using the `pyautogui` library for GUI automation. It opens the Windows Settings, navigates to the Apps section, and searches for the WinRAR application to uninstall it.

## Prerequisites

- Python 3.x
- `pyautogui` library
- `opencv-python` library (for image recognition)
- Screenshots of the necessary UI elements saved in the `img/WinRAR` directory
- `pillow` python library

## Installation

### **Clone the repository**:
```sh
git clone https://github.com/your-repo/your-project.git
cd your-project
```

### **Create and activate a virtual environment**:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **Install the required packages**:
```sh
pip install pyautogui opencv-python pillow
```

### **Ensure the necessary screenshots are available**:
* `settings-apps-menu.png`: Screenshot of the Apps settings menu in Windows Settings.

![Settings Apps Menu](/img/WinRAR/settings-apps-menu.png)

* `installed-apps-menu.png`: Screenshot of the Installed Apps menu in Windows Settings.

![Installed Apps Menu](/img/WinRAR/installed-apps-menu.png)