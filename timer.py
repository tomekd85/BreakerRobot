import time

from Display.OledDisplay.OledDisplay import OledDisplay
from countdowntimer.KeyboardInput import KeyboardInput
from countdowntimer.CountDownTimer import CountDownTimer


if __name__ == '__main__':
    oled = OledDisplay()
    button_input = KeyboardInput()
    timer = CountDownTimer(oled, button_input, 20)
    timer.count()
    time.sleep(3)
