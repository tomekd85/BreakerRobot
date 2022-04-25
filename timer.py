from Display.OledDisplay.OledDisplay import OledDisplay
from countdowntimer.CountDownTimer import CountDownTimer


if __name__ == '__main__':
    oled = OledDisplay(4.5)
    timer = CountDownTimer(oled)
    timer.count(21)
