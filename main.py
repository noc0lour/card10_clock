from utime import sleep
import utime
import display
import buttons
import leds


class Time:
    def __init__(self, clock, start=0):
        self.clock = clock
        self.timeout = 0.1

    def update_once(self):
        with display.open() as disp:
            localtime = utime.localtime()
            self.clock.updateClock(disp, localtime[3], localtime[4], localtime[5])

    def loop(self):
        try:
            with display.open() as disp:
                button_pressed = False
                while True:
                    localtime = utime.localtime()
                    disp.clear()
                    disp = self.clock.updateClock(disp, localtime[3], localtime[4], localtime[5])
                    disp.update()

                    # check for button presses
                    v = buttons.read(buttons.BOTTOM_LEFT |
                                     buttons.BOTTOM_RIGHT)
                    if v == 0:
                        button_pressed = False
                    if not button_pressed and v & buttons.BOTTOM_LEFT != 0:
                        button_pressed = True
                        self.clock.cycleTheme(-1)
                    elif not button_pressed and v & buttons.BOTTOM_RIGHT != 0:
                        button_pressed = True
                        self.clock.cycleTheme(1)
                    sleep(self.timeout)

        except KeyboardInterrupt:
            for i in range(11):
                leds.set(i, (0, 0, 0))
            return
