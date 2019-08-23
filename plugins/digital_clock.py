# 80 x 160 display
# segment length 32 x 2
# top/bottom offset: 5
# left/right offset: 3
# spacing: 2
# line width: 2

import leds


class watch():
    def __init__(self):
        self.col = (255, 255, 255)
        self.led1 = False

    def updateClock(self, disp, hour, minute, second):
        disp = draw_number(disp, hour // 10, offsetx=3, offsety=5)
        disp = draw_number(disp, hour % 10, offsetx=(32 + 6) + 3)
        if second % 2:
            disp = draw_colon(disp, offsetx=(32 + 6) * 2 + 2 + 3)
        self.led1 = toggle_led1(self.led1)
        fill_leds(second // 6)
        if second % 60 == 0:
            for led in range(10):
                leds.set(led + 1, (0, 0, 0))

        disp = draw_number(disp, minute // 10, offsetx=(32 + 6) * 2 + 8 + 3)
        disp = draw_number(disp, minute % 10, offsetx=(32 + 6) * 3 + 8 + 3)
        return disp

    def cycleTheme(self, direction):
        pass


def toggle_led1(value):
    if value:
        leds.set(0, (0, 0, 0))
        return False
    leds.set(0, (255, 255, 255))
    return True


def fill_leds(which_time):
    for led in range(1, which_time + 1):
        color = ((led - 1) * 360 / 10, 1.0, 0.5)
        leds.set_hsv(led, color)


def draw_colon(disp,
               segment_length=32,
               line_width=2,
               offsetx=3,
               offsety=5,
               col=(255, 255, 255)):
    disp = disp.line(
        offsetx,
        offsety + segment_length // 2 + line_width,
        offsetx,
        offsety + segment_length // 2 + 2 * line_width,
        col=col,
        size=line_width)
    disp = disp.line(
        offsetx,
        offsety + int(1.5 * segment_length) + 2 * line_width,
        offsetx,
        offsety + int(1.5 * segment_length) + 3 * line_width,
        col=col,
        size=line_width)
    return disp


def draw_segment(disp,
                 which,
                 segment_length,
                 line_width,
                 offsetx,
                 offsety,
                 col=(255, 255, 255)):
    # A - G : 0 - 6
    if not hasattr(which, "__len__"):
        which = list(which)
    if 0 in which:
        disp = disp.line(
            offsetx + line_width,
            offsety,
            offsetx + segment_length + line_width,
            offsety,
            col=col,
            size=line_width)
    if 1 in which:
        disp = disp.line(
            offsetx + segment_length,
            offsety,
            offsetx + segment_length,
            offsety + segment_length,
            col=col,
            size=line_width)
    if 2 in which:
        disp = disp.line(
            offsetx + segment_length,
            offsety + segment_length + line_width,
            offsetx + segment_length,
            offsety + segment_length * 2 + line_width,
            col=col,
            size=line_width)
    if 3 in which:
        disp = disp.line(
            offsetx + line_width,
            offsety + segment_length * 2 + line_width,
            offsetx + segment_length + line_width,
            offsety + segment_length * 2 + line_width,
            col=col,
            size=line_width)
    if 4 in which:
        disp = disp.line(
            offsetx,
            offsety + segment_length + line_width,
            offsetx,
            offsety + 2 * segment_length + line_width,
            col=col,
            size=line_width)
    if 5 in which:
        disp = disp.line(
            offsetx,
            offsety + line_width,
            offsetx,
            offsety + segment_length + line_width,
            col=col,
            size=line_width)
    if 6 in which:
        disp = disp.line(
            offsetx + line_width,
            offsety + segment_length + line_width,
            offsetx + line_width + segment_length,
            offsety + segment_length + line_width,
            col=col,
            size=line_width)
    return disp


def draw_number(disp,
                number,
                line_width=1,
                segment_length=32,
                offsetx=3,
                offsety=5):
    if number == 0:
        return draw_segment(disp, (0, 1, 2, 3, 4, 5), segment_length,
                            line_width, offsetx, offsety)
    if number == 1:
        return draw_segment(disp, (1, 2), segment_length, line_width, offsetx,
                            offsety)
    if number == 2:
        return draw_segment(disp, (0, 1, 6, 4, 3), segment_length, line_width,
                            offsetx, offsety)
    if number == 3:
        return draw_segment(disp, (0, 1, 6, 2, 3), segment_length, line_width,
                            offsetx, offsety)
    if number == 4:
        return draw_segment(disp, (5, 6, 1, 2), segment_length, line_width,
                            offsetx, offsety)
    if number == 5:
        return draw_segment(disp, (0, 5, 6, 2, 3), segment_length, line_width,
                            offsetx, offsety)
    if number == 6:
        return draw_segment(disp, (0, 5, 6, 2, 3, 4), segment_length,
                            line_width, offsetx, offsety)
    if number == 7:
        return draw_segment(disp, (0, 1, 2), segment_length, line_width,
                            offsetx, offsety)
    if number == 8:
        return draw_segment(disp, (0, 1, 2, 3, 4, 5, 6), segment_length,
                            line_width, offsetx, offsety)
    if number == 9:
        return draw_segment(disp, (0, 1, 2, 3, 5, 6), segment_length,
                            line_width, offsetx, offsety)
