import pyautogui
import os
import time
import subprocess

class ChromeYouTubeAutomator:
    def __init__(self, youtube_channel):
        self.youtube_channel = youtube_channel

    def open_chrome(self):
        # Open Google Chrome on macOS
        subprocess.run(["open", "-a", "Google Chrome"])
        time.sleep(5)  # Wait for Chrome to open

        # Type YouTube URL and press Enter
        pyautogui.typewrite('https://www.youtube.com')
        pyautogui.press('enter')
        time.sleep(2)  # Wait for YouTube to load

        # Click on the search bar
        search_bar_location = pyautogui.locateCenterOnScreen('img/youtube_search_bar.png', confidence=0.8)
        if search_bar_location:
            pyautogui.click(search_bar_location)
            time.sleep(1)

            # Type the YouTube channel name and press Enter
            pyautogui.typewrite(self.youtube_channel)
            pyautogui.press('enter')
            time.sleep(2)  # Wait for search results to load
        else:
            print("YouTube search bar not found on screen.")
        
        subscribe_button = pyautogui.locateCenterOnScreen('img/youtube_subscribe_button.png', confidence=0.8)
        if search_bar_location:
            pyautogui.click(subscribe_button)
            pyautogui.press('enter')
            time.sleep(1)

        else:
            print("YouTube subscribe button not found on screen.")

    def automate(self):
        self.open_chrome()

# Example usage:
if __name__ == "__main__":
    automator = ChromeYouTubeAutomator(youtube_channel="Ben Rector")
    automator.automate()