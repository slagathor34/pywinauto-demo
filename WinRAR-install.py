"""
WinRAR Installer Automation Script
==================================

This script automates the installation of WinRAR using pywinauto_recorder.

Functions:
----------
- start_winrar_installer: Starts the WinRAR installer.
- automate_installation: Automates the installation process by interacting with the installer UI.
"""

import os
from pywinauto_recorder.player import *

def start_winrar_installer():
    """
    Start the WinRAR installer.

    This function starts the WinRAR installer executable.
    """
    os.startfile("WinRAR-701.exe")

def automate_installation():
    """
    Automate the WinRAR installation process.

    This function interacts with the WinRAR installer UI to automate the installation process.
    """
    try:
        with UIPath(u"WinRAR ||Window"):
            print("WinRAR window found")
            element = find(u"Next >||Button", timeout=5)
            if element:
                click(u"Next >||Button")
                print("Clicked 'Next >' button")
            else:
                print("Failed to find 'Next >' button")
            
            element = find(u"Custom Setup||RadioButton", timeout=5)
            if element:
                click(u"Custom Setup||RadioButton")
                print("Clicked 'Custom Setup' radio button")
            else:
                print("Failed to find 'Custom Setup' radio button")
            
            element = find(u"Next >||Button", timeout=5)
            if element:
                click(u"Next >||Button")
                print("Clicked 'Next >' button")
            else:
                print("Failed to find 'Next >' button")
            
            element = find(u"I accept the terms of the EULA||CheckBox", timeout=5)
            if element:
                click(u"I accept the terms of the EULA||CheckBox")
                print("Clicked 'I accept the terms of the EULA' checkbox")
            else:
                print("Failed to find 'I accept the terms of the EULA' checkbox")
            
            element = find(u"Next||Button", timeout=5)
            if element:
                click(u"Next||Button")
                print("Clicked 'Next' button")
            else:
                print("Failed to find 'Next' button")
            
            element = find(u"||Edit", timeout=5)
            if element:
                click(u"||Edit")
                send_keys("-custom")
                print("Clicked 'Edit' field and entered '-custom'")
            else:
                print("Failed to find 'Edit' field to enter '-custom'")
            
            element = find(u"Install||Button", timeout=5)
            if element:
                click(u"Install||Button")
                print("Clicked 'Install' button")
            else:
                print("Failed to find 'Install' button")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with UIPath(u"WinRAR Setup||Window"):
            print("WinRAR Setup window found")
            element = find(u"OK||Button", timeout=40)
            if element:
                click(u"OK||Button")
                print("Clicked 'OK' button")
            else:
                print("Failed to find 'OK' button")
            
            element = find(u"Done||Button", timeout=5)
            if element:
                click(u"Done||Button")
                print("Clicked 'Done' button")
            else:
                print("Failed to find 'Done' button")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_winrar_installer()
    automate_installation()
