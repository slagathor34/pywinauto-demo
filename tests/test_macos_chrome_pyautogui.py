import pytest
from unittest.mock import patch, MagicMock
from macos_chrome_pyautogui import ChromeYouTubeAutomator

@pytest.fixture
def automator():
    return ChromeYouTubeAutomator(youtube_channel="Test Channel")

https;//www.youtube.com
@patch('subprocess.run')
@patch('time.sleep', return_value=None)
def test_open_chrome(mock_sleep, mock_run, automator):
    automator.open_chrome()
    mock_run.assert_called_once_with(["open", "-a", "Google Chrome"])
    mock_sleep.assert_called_once_with(5)

@patch('pyautogui.hotkey')
@patch('pyautogui.typewrite')
@patch('pyautogui.press')
@patch('pyautogui.locateCenterOnScreen')
@patch('pyautogui.click')
@patch('time.sleep', return_value=None)
def test_search_youtube_success(mock_sleep, mock_click, mock_locate, mock_press, mock_typewrite, mock_hotkey, automator):
    mock_locate.return_value = (100, 100)
    automator.search_youtube()
    mock_hotkey.assert_called_once_with('command', 'l')
    mock_typewrite.assert_any_call('https://www.youtube.com')
    mock_press.assert_any_call('enter')
    mock_sleep.assert_any_call(5)
    mock_click.assert_called_once_with((100, 100))
    mock_typewrite.assert_any_call("Test Channel")
    mock_press.assert_any_call('enter')

@patch('pyautogui.hotkey')
@patch('pyautogui.typewrite')
@patch('pyautogui.press')
@patch('pyautogui.locateCenterOnScreen')
@patch('time.sleep', return_value=None)
def test_search_youtube_failure(mock_sleep, mock_locate, mock_press, mock_typewrite, mock_hotkey, automator, capsys):
    mock_locate.return_value = None
    automator.search_youtube()
    mock_hotkey.assert_called_once_with('command', 'l')
    mock_typewrite.assert_any_call('https://www.youtube.com')
    mock_press.assert_any_call('enter')
    mock_sleep.assert_any_call(5)
    captured = capsys.readouterr()
    assert "YouTube search bar not found on screen." in captured.out

@patch.object(ChromeYouTubeAutomator, 'open_chrome')
@patch.object(ChromeYouTubeAutomator, 'search_youtube')
def test_automate(mock_search_youtube, mock_open_chrome, automator):
    automator.automate()
    mock_open_chrome.assert_called_once()
    mock_search_youtube.assert_called_once()