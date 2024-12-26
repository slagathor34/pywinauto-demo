import pyautogui
import os
import time
import subprocess

class WinRARUninstallAutomator:
    def __init__(self, app_name):
        self.app_name = app_name

    def open_settings(self):
        # Open Settings on Windows 11
        subprocess.run(["start", "ms-settings:"], shell=True)
        time.sleep(5)  # Wait for Settings to open

        # Click on the Apps settings option
        settings_app_location = pyautogui.locateCenterOnScreen('img/WinRAR/settings-apps-menu.png', confidence=0.8)
        if settings_app_location:
            pyautogui.click(settings_app_location)
            time.sleep(1)
        else:
            print("App settings panel not found on screen.")

        # Click on the search bar
        installed_app_location = pyautogui.locateCenterOnScreen('img/WinRAR/installed-apps-menu.png', confidence=0.4)
        if installed_app_location:
            pyautogui.click(installed_app_location)
            time.sleep(3)
        else:
            print("Installed App settings panel not found on screen.")

        pyautogui.typewrite(self.app_name)
        time.sleep(1)
        pyautogui.press('enter')

        uninstall_menu_location = pyautogui.locateCenterOnScreen('img/WinRAR/apps-hamburger.png', confidence=0.8)
        if uninstall_menu_location:
            pyautogui.click(uninstall_menu_location)
            time.sleep(1)
        else:
            print("Uninstall menu not found on screen.")
        
        uninstall_button_location = pyautogui.locateCenterOnScreen('img/WinRAR/apps-uninstall-button.png', confidence=0.8)
        if uninstall_button_location:
            pyautogui.press('enter')
            time.sleep(1)
        else:
            print("Uninstall button not found on screen.")
        
        uninstall_confirm_button_location = pyautogui.locateCenterOnScreen('img/WinRAR/apps-confirm-uninstall-button.png', confidence=0.3)
        if uninstall_confirm_button_location:
            pyautogui.press('enter')
            time.sleep(1)
        else:
            print("Uninstall button not found on screen.")
        
        continue_with_uninstall_button_location = pyautogui.locateCenterOnScreen('img/WinRAR/continue_with_winrar_uninstall.png', confidence=0.5)
        if continue_with_uninstall_button_location:
            pyautogui.click(continue_with_uninstall_button_location)
            time.sleep(3)
            pyautogui.hotkey('alt', 'f4')
        else:
            print("Uninstall button not found on screen.")

    def automate(self):
        self.open_settings()

# Example usage:
if __name__ == "__main__":
    automator = WinRARUninstallAutomator(app_name="WinRAR")
    automator.automate()