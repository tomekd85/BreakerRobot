import os

from Display.OledDisplay.OledDisplay import OledDisplay
from countdowntimer.CountDownTimer import CountDownTimer


if __name__ == '__main__':
    oled = OledDisplay()
    if os.uname().machine.startswith("arm"):
        from countdowntimer.ButtonInput import ButtonInput
        from Beeper.RpiBeeper import RpiBeeper
        button_input = ButtonInput()
        timer_seconds = 25 * 60
        buzzer = RpiBeeper()
    else:
        from countdowntimer.KeyboardInput import KeyboardInput
        from Beeper.DefaultBeeper import DefaultBeeper
        button_input = KeyboardInput()
        timer_seconds = 15
        buzzer = DefaultBeeper()
    timer = CountDownTimer(oled, button_input, timer_seconds, buzzer)
    while True:
        timer.count()
