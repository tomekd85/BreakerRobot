from Beeper import Beeper


class DefaultBeeper(Beeper):
    def beep(self, time):
        print("Beeped for %s seconds" % time)
