from math import sqrt

colors = {
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

firstCH = {
    " ": 'white',
    ".": 'white',
    "'": 'white',
    ",": 'white',
    ";": 'white',
    ":": 'white',
    "c": 'white',
    "l": 'white',
    "o": 'white',
    "d": 'grey',
    "x": 'grey',
    "k": 'grey',
    "O": 'grey',
    "0": 'grey',
    "K": 'grey',
    "X": 'grey',
    "N": 'grey',
    "W": 'grey',
    "M": 'grey',
}


def get_rgb(rgb_pixel):
    distance = {get_distance(rgb_pixel, 'red'): 'red',
                get_distance(rgb_pixel, 'yellow'): 'yellow',
                get_distance(rgb_pixel, 'magenta'): 'magenta',
                get_distance(rgb_pixel, 'white'): 'white',
                get_distance(rgb_pixel, 'green'): 'green',
                get_distance(rgb_pixel, 'blue'): 'blue',
                get_distance(rgb_pixel, 'cyan'): 'cyan',
                get_distance(rgb_pixel, 'grey'): 'grey',
                get_distance(rgb_pixel, 'black'): 'grey'}
    return distance[min(distance)]


def get_rgb_symbol(ch):
    return firstCH[ch]


def get_distance(rgb_pixel, color):
    return sqrt((rgb_pixel[0] - colors[color][0]) ** 2 +
                (rgb_pixel[1] - colors[color][1]) ** 2 +
                (rgb_pixel[2] - colors[color][2]) ** 2)
