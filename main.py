"""
This Script helps you install a big collection of Mods in Vortex without the need of Premium.
Vortex is forcing you to buy premium by making you install each mod in the collection manually one after another.
if a Mods needs to be downloaded, a popup in Vortex appears to lead you to the download page (first download button).
On the Website you have to click another Button (second download button).
If you restart the installation of the mods at any point, Vortex will ask you if you want to reinstall the mod or
if you want to install it beside the already installed mod (that's the continue button. it will reinstall the mod)

pyautogui only checks the main Screen. So make sure that Vortex and one Browser that will open the links is on the same
Screen. Ideally side by side.
Maybe the button images needs to be modified to fit the screen and windows resolution.
"""

from time import sleep

import pyautogui


# image = pyautogui.screenshot()
# image.save('testing.png')


def click_button(picture_name: str, custom_confidence=None):
    current_position = False
    last_position = False
    try_to_solve: int = 0
    while try_to_solve < 5:
        if current_position := pyautogui.locateOnScreen(picture_name, grayscale=False, confidence=custom_confidence):
            if current_position == last_position:
                pyautogui.click(current_position)
                return True
            else:
                last_position = current_position
                try_to_solve += 1
        else:
            break
    return False


if __name__ == '__main__':
    while True:
        if click_button("Download.png", custom_confidence=0.8):
            print("\nPressed first download button. Wait 5 Seconds.")
            sleep(5)
            if click_button("Download2.png", custom_confidence=0.8):
                print("Pressed download button. Wait 10 Seconds.")
                sleep(10)
            else:
                print("Second download button not found!")
        elif click_button("Continue.png", custom_confidence=0.95):
            print("\nPressed Continue Button")
            sleep(1)
        else:
            print(".", end="")
            sleep(1)

    # Old Version
    # while True:
    #     current_location = False
    #     verified_position = False
    #     # print("looking for first button")
    #     if current_location := pyautogui.locateOnScreen('Download.png', grayscale=False, confidence=.8):
    #         print("\nFound first download button")
    #         print(current_location)
    #         pyautogui.click(current_location)
    #         sleep(5)
    #
    #         # print("looking for second button")
    #         current_location = False
    #         if current_location := pyautogui.locateOnScreen('Download2.png', grayscale=False, confidence=.8):
    #             print("Found second download button")
    #             print(current_location)
    #             pyautogui.click(current_location)
    #             sleep(10)
    #         else:
    #             print("Second download button not found!")
    #     elif current_location := pyautogui.locateOnScreen('Continue.png', grayscale=False, confidence=.95):
    #         print("\nFound Continue Button")
    #         print(current_location)
    #         pyautogui.click(current_location)
    #         sleep(1)
    #     else:
    #         print(".", end="")
    #         sleep(1)
