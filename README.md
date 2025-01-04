# Windows UI Automation with Python

This project automates the user interface of Windows 11 and Windows Server using Python3 and the `pywinauto`, `pyautogui`, `opencv-python`, and `pillow` libraries. It includes setting up a virtual environment, installing packages from a verified Artifactory repository, executing the automation script, and cleaning up the environment after execution.

## Prerequisites

- Python 3.x
- `pywinauto` library
- `pyautogui` library
- `opencv-python` library
- `pillow` library
- Access to a verified JFrog Artifactory repository

## Installation

### Clone the Repository

```sh
git clone https://github.com/your-repo/your-project.git
```

## Workflow
```mermaid
  graph TD
    A[Start Script] --> B[Initialize WinRARUninstallAutomator]
    B --> C[Open Settings]
    C --> D{Settings Opened?}
    D -->|Yes| E[Click on Apps Settings Option]
    D -->|No| F[Print App settings panel not found]
    E --> G{Apps Settings Option Clicked?}
    G -->|Yes| H[Click on Installed Apps Menu]
    G -->|No| I[Print Installed App settings panel not found]
    H --> J{Installed Apps Menu Clicked?}
    J -->|Yes| K[Proceed with Uninstallation Steps]
    J -->|No| L[Print Installed App settings panel not found]
    K --> M[End Script]
```