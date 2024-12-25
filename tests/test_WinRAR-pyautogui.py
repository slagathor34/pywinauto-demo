import pytest
from unittest.mock import patch, MagicMock
from WinRAR_pyautogui import WinRARInstaller

@pytest.fixture
def installer():
    return WinRARInstaller(
        installer_path="/path/to/WinRAR-installer.exe",
        next_button_image="next_button.png",
        install_button_image="install_button.png",
        finish_button_image="finish_button.png"
    )

@patch('pyautogui.locateCenterOnScreen')
@patch('pyautogui.click')
def test_click_image_success(mock_click, mock_locate, installer):
    mock_locate.return_value = (100, 100)
    result = installer.click_image("next_button.png")
    assert result is True
    mock_click.assert_called_once_with((100, 100))

@patch('pyautogui.locateCenterOnScreen')
def test_click_image_failure(mock_locate, installer):
    mock_locate.return_value = None
    result = installer.click_image("next_button.png")
    assert result is False

@patch('os.startfile')
@patch('time.sleep', return_value=None)
@patch.object(WinRARInstaller, 'click_image')
def test_install_winrar_success(mock_click_image, mock_sleep, mock_startfile, installer):
    mock_click_image.side_effect = [True, True, True]
    result = installer.install_winrar()
    assert result is True
    mock_startfile.assert_called_once_with("/path/to/WinRAR-installer.exe")
    assert mock_click_image.call_count == 3

@patch('os.startfile')
@patch('time.sleep', return_value=None)
@patch.object(WinRARInstaller, 'click_image')
def test_install_winrar_failure(mock_click_image, mock_sleep, mock_startfile, installer):
    mock_click_image.side_effect = [True, False, True]
    result = installer.install_winrar()
    assert result is False
    mock_startfile.assert_called_once_with("/path/to/WinRAR-installer.exe")
    assert mock_click_image.call_count == 2