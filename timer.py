import os

from Display.OledDisplay.OledDisplay import OledDisplay
from countdowntimer.CountDownTimer import CountDownTimer


if __name__ == '__main__':
    oled = OledDisplay()
    if os.uname().machine.startswith("arm"):
        from countdowntimer.ButtonInput import ButtonInput
        button_input = ButtonInput()
        timer_seconds = 25 * 60
    else:
        from countdowntimer.KeyboardInput import KeyboardInput
        button_input = KeyboardInput()
        timer_seconds = 15
    timer = CountDownTimer(oled, button_input, timer_seconds)
    while True:
        timer.count()
