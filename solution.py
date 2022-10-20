LIGHT_COLORS = {'light_green': 'C0FFC0', 'light_yellow': 'FFFFC0', 'light_red': 'FFC0C0', 'light_blue': 'C0C0FF'}
DARK_COLORS = {'dark_green': '00C000', 'dark_yellow': 'C0C000', 'dark_red': 'C00000', 'dark_blue': '0000C0'}
BLACK_COLOR = '000000'
WHITE_COLOR = 'FFFFFF'


def validate_the_arguments(coordinates, colors):
    # First argument should be a tuple with len = 2
    if type(coordinates) is not tuple or len(coordinates) != 2:
        raise TypeError("First argument must be tuple with two elements (coordinates exam: (1, 1))")

    # Second argument should be a list
    if type(colors) is not list:
        raise TypeError("Second argument must be a list which contains colors(exam: ['00C000', 'C0FFC0', 'C00000'])")

    # Second argument should contain only the given colors
    for color in colors:
        if color.upper() not in DARK_COLORS.values() and color.upper() not in LIGHT_COLORS.values()\
                and color.upper() != BLACK_COLOR and color.upper() != WHITE_COLOR:
            raise AssertionError("""Second argument should contain only the given colors:
            light_green -> C0FFC0
            light_yellow -> FFFFC0
            light_red -> FFC0C0
            light_blue -> C0C0FF
            dark_green -> 00C000
            dark_yellow -> C0C000
            dark_red -> C00000
            dark_blue -> 0000C0
            black -> 000000
            white -> FFFFFF
            """)


def calculate_final_vector(coordinates, colors):
    validate_the_arguments(coordinates, colors)
    # First argument is a tuple(it is immutable), so to change the coordinates we need to pass them in new variables
    x2 = coordinates[0]
    y2 = coordinates[1]

    for color in colors:
        # For the coordinates light_blue is the same as dark_yellow, so it can be one case
        if color.upper() == LIGHT_COLORS['light_blue'] or color.upper() == DARK_COLORS['dark_yellow']:
            y2 += 1
        # For the coordinates light_yellow is the same as dark_blue, so it can be one case
        elif color.upper() == LIGHT_COLORS['light_yellow'] or color.upper() == DARK_COLORS['dark_blue']:
            y2 -= 1
        # For the coordinates light_green is the same as dark_red, so it can be one case
        elif color.upper() == LIGHT_COLORS['light_green'] or color.upper() == DARK_COLORS['dark_red']:
            x2 -= 1
        # For the coordinates light_red is the same as dark_green, so it can be one case
        elif color.upper() == LIGHT_COLORS['light_red'] or color.upper() == DARK_COLORS['dark_green']:
            x2 += 1
        elif color.upper() == WHITE_COLOR:
            continue
        elif color.upper() == BLACK_COLOR:
            break
        else:
            raise AssertionError('There is no way to be here! :)')

    return x2, y2
