import pyautogui
import os
import time

class WinRARInstaller:
    def __init__(self, installer_path, next_button_image, install_button_image, finish_button_image):
        self.installer_path = installer_path
        self.next_button_image = next_button_image
        self.install_button_image = install_button_image
        self.finish_button_image = finish_button_image

    def click_image(self, image_path, confidence=0.8):
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        else:
            print(f"Image {image_path} not found on screen.")
            return False

    def install_winrar(self):
        os.startfile(self.installer_path)
        time.sleep(5)  # Wait for the installer to open

        if not self.click_image(self.next_button_image):
            return False
        time.sleep(2)

        if not self.click_image(self.install_button_image):
            return False
        time.sleep(10)  # Wait for the installation to complete

        if not self.click_image(self.finish_button_image):
            return False
        time.sleep(2)

        print("WinRAR installation completed.")
        return True

# Example usage:
if __name__ == "__main__":
    installer = WinRARInstaller(
        installer_path="/path/to/WinRAR-installer.exe",
        next_button_image="next_button.png",
        install_button_image="install_button.png",
        finish_button_image="finish_button.png"
    )
    installer.install_winrar()