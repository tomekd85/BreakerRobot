import os
import time

from Display.OledDisplay.OledDisplay import OledDisplay
from countdowntimer.CountDownTimer import CountDownTimer


if __name__ == '__main__':
    oled = OledDisplay()
    if os.uname().machine.startswith("arm"):
        from countdowntimer.ButtonInput import ButtonInput
        button_input = ButtonInput()
    else:
        from countdowntimer.KeyboardInput import KeyboardInput
        button_input = KeyboardInput()
    timer = CountDownTimer(oled, button_input, 20)
    timer.count()
    time.sleep(3)
