import pyautogui
import pyperclip
import time


# Step 1: Click on the icon at (115, 745)
pyautogui.click(315, 750)
time.sleep(1)  # Wait for 1 second to ensure the UI reacts

# Step 2: Drag from (53, 65) to (1231, 700) to select text
pyautogui.moveTo(114, 136)
pyautogui.mouseDown()  # Press the mouse button
pyautogui.moveTo(114, 270, duration=1)  # Drag to the end point
pyautogui.mouseUp()  # Release the mouse button

# Step 3: Press Ctrl+C (or Command+C on macOS) to copy the selected text
pyautogui.hotkey("ctrl", "c")  # For Windows/Linux
# pyautogui.hotkey("command", "c")  # Uncomment this for macOS
time.sleep(1)  # Wait for the copy operation to complete

# Step 4: Get the text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text to verify
print("Copied Text:", copied_text)