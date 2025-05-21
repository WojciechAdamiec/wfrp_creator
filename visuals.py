from itertools import cycle


COLORS = ["cyan", "magenta", "green", "red", "yellow", "blue", "purple", "dark_goldenrod", "deep_sky_blue1", "dark_khaki"]


def get_color_cycle():
    return cycle(COLORS)
