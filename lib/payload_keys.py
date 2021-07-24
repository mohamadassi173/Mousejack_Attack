def payload_keys(key):
    keys = {
        'ctrl+shift+enter': [0, 193, 3, 40, 0, 0, 0, 0, 0, 20],
        'ctrl+esc': [0, 193, 1, 41, 0, 0, 0, 0, 0, 21],
        'hideDesktop': [0, 193, 8, 7, 0, 0, 0, 0, 0, 48],  # GUI + d
        'run': [0, 193, 8, 21, 0, 0, 0, 0, 0, 34],  # GUI + r
        'init': [0, 79, 0, 4, 176, 16, 0, 0, 0, 237],
        'wait': [0, 64, 4, 176, 12],  # keepalive
        '': [0, 193, 0, 0, 0, 0, 0, 0, 0, 63],
        'ALT': [0, 193, 4, 0, 0, 0, 0, 0, 0, 59],
        'SHIFT': [0, 193, 2, 0, 0, 0, 0, 0, 0, 61],
        'CTRL': [0, 193, 1, 0, 0, 0, 0, 0, 0, 62],
        'GUI': [0, 193, 8, 0, 0, 0, 0, 0, 0, 55],
        'SCROLLLOCK': [0, 193, 0, 71, 0, 0, 0, 0, 0, -8],
        'ENTER': [0, 193, 0, 40, 0, 0, 0, 0, 0, 23],
        'F12': [0, 193, 0, 69, 0, 0, 0, 0, 0, -6],
        'HOME': [0, 193, 0, 74, 0, 0, 0, 0, 0, -11],
        'F10': [0, 193, 0, 67, 0, 0, 0, 0, 0, -4],
        'F9': [0, 193, 0, 66, 0, 0, 0, 0, 0, -3],
        'ESCAPE': [0, 193, 0, 41, 0, 0, 0, 0, 0, 22],
        'PAGEUP': [0, 193, 0, 75, 0, 0, 0, 0, 0, -12],
        'TAB': [0, 193, 0, 43, 0, 0, 0, 0, 0, 20],
        'PRINTSCREEN': [0, 193, 0, 70, 0, 0, 0, 0, 0, -7],
        'F2': [0, 193, 0, 59, 0, 0, 0, 0, 0, 4],
        'CAPSLOCK': [0, 193, 0, 57, 0, 0, 0, 0, 0, 6],
        'F1': [0, 193, 0, 58, 0, 0, 0, 0, 0, 5],
        'F4': [0, 193, 0, 61, 0, 0, 0, 0, 0, 2],
        'F6': [0, 193, 0, 63, 0, 0, 0, 0, 0, 0],
        'F8': [0, 193, 0, 65, 0, 0, 0, 0, 0, -2],
        'DOWNARROW': [0, 193, 0, 81, 0, 0, 0, 0, 0, -18],
        'DELETE': [0, 193, 0, 42, 0, 0, 0, 0, 0, 21],
        'RIGHT': [0, 193, 0, 79, 0, 0, 0, 0, 0, -16],
        'F3': [0, 193, 0, 60, 0, 0, 0, 0, 0, 3],
        'DOWN': [0, 193, 0, 81, 0, 0, 0, 0, 0, -18],
        'DEL': [0, 193, 0, 76, 0, 0, 0, 0, 0, -13],
        'END': [0, 193, 0, 77, 0, 0, 0, 0, 0, -14],
        'INSERT': [0, 193, 0, 73, 0, 0, 0, 0, 0, -10],
        'F5': [0, 193, 0, 62, 0, 0, 0, 0, 0, 1],
        'LEFTARROW': [0, 193, 0, 80, 0, 0, 0, 0, 0, -17],
        'RIGHTARROW': [0, 193, 0, 79, 0, 0, 0, 0, 0, -16],
        'PAGEDOWN': [0, 193, 0, 78, 0, 0, 0, 0, 0, -15],
        'PAUSE': [0, 193, 0, 72, 0, 0, 0, 0, 0, -9],
        'SPACE': [0, 193, 0, 44, 0, 0, 0, 0, 0, 19],
        'UPARROW': [0, 193, 0, 82, 0, 0, 0, 0, 0, -19],
        'F11': [0, 193, 0, 68, 0, 0, 0, 0, 0, -5],
        'F7': [0, 193, 0, 64, 0, 0, 0, 0, 0, -1],
        'UP': [0, 193, 0, 82, 0, 0, 0, 0, 0, -19],
        'LEFT': [0, 193, 0, 80, 0, 0, 0, 0, 0, -17],
        " ": [0, 193, 0, 44, 0, 0, 0, 0, 0, 19],
        "!": [0, 193, 2, 30, 0, 0, 0, 0, 0, 31],
        "\"": [0, 193, 2, 52, 0, 0, 0, 0, 0, 9],
        "#": [0, 193, 2, 32, 0, 0, 0, 0, 0, 29],
        "$": [0, 193, 2, 33, 0, 0, 0, 0, 0, 28],
        "%": [0, 193, 2, 34, 0, 0, 0, 0, 0, 27],
        "&": [0, 193, 2, 36, 0, 0, 0, 0, 0, 25],
        "'": [0, 193, 0, 52, 0, 0, 0, 0, 0, 11],
        "(": [0, 193, 2, 38, 0, 0, 0, 0, 0, 23],
        ")": [0, 193, 2, 39, 0, 0, 0, 0, 0, 22],
        "*": [0, 193, 2, 37, 0, 0, 0, 0, 0, 24],
        "+": [0, 193, 2, 46, 0, 0, 0, 0, 0, 15],
        ",": [0, 193, 0, 54, 0, 0, 0, 0, 0, 9],
        "-": [0, 193, 0, 45, 0, 0, 0, 0, 0, 18],
        ".": [0, 193, 0, 55, 0, 0, 0, 0, 0, 8],
        "/": [0, 193, 0, 56, 0, 0, 0, 0, 0, 7],
        "0": [0, 193, 0, 39, 0, 0, 0, 0, 0, 24],
        "1": [0, 193, 0, 30, 0, 0, 0, 0, 0, 33],
        "2": [0, 193, 0, 31, 0, 0, 0, 0, 0, 32],
        "3": [0, 193, 0, 32, 0, 0, 0, 0, 0, 31],
        "4": [0, 193, 0, 33, 0, 0, 0, 0, 0, 30],
        "5": [0, 193, 0, 34, 0, 0, 0, 0, 0, 29],
        "6": [0, 193, 0, 35, 0, 0, 0, 0, 0, 28],
        "7": [0, 193, 0, 36, 0, 0, 0, 0, 0, 27],
        "8": [0, 193, 0, 37, 0, 0, 0, 0, 0, 26],
        "9": [0, 193, 0, 38, 0, 0, 0, 0, 0, 25],
        ":": [0, 193, 2, 51, 0, 0, 0, 0, 0, 10],
        ";": [0, 193, 0, 51, 0, 0, 0, 0, 0, 12],
        "<": [0, 193, 2, 54, 0, 0, 0, 0, 0, 7],
        "=": [0, 193, 0, 46, 0, 0, 0, 0, 0, 17],
        ">": [0, 193, 2, 55, 0, 0, 0, 0, 0, 6],
        "?": [0, 193, 2, 56, 0, 0, 0, 0, 0, 5],
        "@": [0, 193, 2, 31, 0, 0, 0, 0, 0, 30],
        "A": [0, 193, 2, 4, 0, 0, 0, 0, 0, 57],
        "B": [0, 193, 2, 5, 0, 0, 0, 0, 0, 56],
        "C": [0, 193, 2, 6, 0, 0, 0, 0, 0, 55],
        "D": [0, 193, 2, 7, 0, 0, 0, 0, 0, 54],
        "E": [0, 193, 2, 8, 0, 0, 0, 0, 0, 53],
        "F": [0, 193, 2, 9, 0, 0, 0, 0, 0, 52],
        "G": [0, 193, 2, 10, 0, 0, 0, 0, 0, 51],
        "H": [0, 193, 2, 11, 0, 0, 0, 0, 0, 50],
        "I": [0, 193, 2, 12, 0, 0, 0, 0, 0, 49],
        "J": [0, 193, 2, 13, 0, 0, 0, 0, 0, 48],
        "K": [0, 193, 2, 14, 0, 0, 0, 0, 0, 47],
        "L": [0, 193, 2, 15, 0, 0, 0, 0, 0, 46],
        "M": [0, 193, 2, 16, 0, 0, 0, 0, 0, 45],
        "N": [0, 193, 2, 17, 0, 0, 0, 0, 0, 44],
        "O": [0, 193, 2, 18, 0, 0, 0, 0, 0, 43],
        "P": [0, 193, 2, 19, 0, 0, 0, 0, 0, 42],
        "Q": [0, 193, 2, 20, 0, 0, 0, 0, 0, 41],
        "R": [0, 193, 2, 21, 0, 0, 0, 0, 0, 40],
        "S": [0, 193, 2, 22, 0, 0, 0, 0, 0, 39],
        "T": [0, 193, 2, 23, 0, 0, 0, 0, 0, 38],
        "U": [0, 193, 2, 24, 0, 0, 0, 0, 0, 37],
        "V": [0, 193, 2, 25, 0, 0, 0, 0, 0, 36],
        "W": [0, 193, 2, 26, 0, 0, 0, 0, 0, 35],
        "X": [0, 193, 2, 27, 0, 0, 0, 0, 0, 34],
        "Y": [0, 193, 2, 28, 0, 0, 0, 0, 0, 33],
        "Z": [0, 193, 2, 29, 0, 0, 0, 0, 0, 32],
        "[": [0, 193, 0, 47, 0, 0, 0, 0, 0, 16],
        "\\": [0, 193, 0, 49, 0, 0, 0, 0, 0, 14],
        "]": [0, 193, 0, 48, 0, 0, 0, 0, 0, 15],
        "^": [0, 193, 2, 35, 0, 0, 0, 0, 0, 26],
        "_": [0, 193, 2, 45, 0, 0, 0, 0, 0, 16],
        "`": [0, 193, 0, 53, 0, 0, 0, 0, 0, 10],
        "a": [0, 193, 0, 4, 0, 0, 0, 0, 0, 59],
        "b": [0, 193, 0, 5, 0, 0, 0, 0, 0, 58],
        "c": [0, 193, 0, 6, 0, 0, 0, 0, 0, 57],
        "d": [0, 193, 0, 7, 0, 0, 0, 0, 0, 56],
        "e": [0, 193, 0, 8, 0, 0, 0, 0, 0, 55],
        "f": [0, 193, 0, 9, 0, 0, 0, 0, 0, 54],
        "g": [0, 193, 0, 10, 0, 0, 0, 0, 0, 53],
        "h": [0, 193, 0, 11, 0, 0, 0, 0, 0, 52],
        "i": [0, 193, 0, 12, 0, 0, 0, 0, 0, 51],
        "j": [0, 193, 0, 13, 0, 0, 0, 0, 0, 50],
        "k": [0, 193, 0, 14, 0, 0, 0, 0, 0, 49],
        "l": [0, 193, 0, 15, 0, 0, 0, 0, 0, 48],
        "m": [0, 193, 0, 16, 0, 0, 0, 0, 0, 47],
        "n": [0, 193, 0, 17, 0, 0, 0, 0, 0, 46],
        "o": [0, 193, 0, 18, 0, 0, 0, 0, 0, 45],
        "p": [0, 193, 0, 19, 0, 0, 0, 0, 0, 44],
        "q": [0, 193, 0, 20, 0, 0, 0, 0, 0, 43],
        "r": [0, 193, 0, 21, 0, 0, 0, 0, 0, 42],
        "s": [0, 193, 0, 22, 0, 0, 0, 0, 0, 41],
        "t": [0, 193, 0, 23, 0, 0, 0, 0, 0, 40],
        "u": [0, 193, 0, 24, 0, 0, 0, 0, 0, 39],
        "v": [0, 193, 0, 25, 0, 0, 0, 0, 0, 38],
        "w": [0, 193, 0, 26, 0, 0, 0, 0, 0, 37],
        "x": [0, 193, 0, 27, 0, 0, 0, 0, 0, 36],
        "y": [0, 193, 0, 28, 0, 0, 0, 0, 0, 35],
        "z": [0, 193, 0, 29, 0, 0, 0, 0, 0, 34],
        "{": [0, 193, 2, 47, 0, 0, 0, 0, 0, 14],
        "|": [0, 193, 2, 49, 0, 0, 0, 0, 0, 12],
        "}": [0, 193, 2, 48, 0, 0, 0, 0, 0, 13],
        "~": [0, 193, 2, 53, 0, 0, 0, 0, 0, 8],
        "BACKSPACE": [0, 193, 0, 42, 0, 0, 0, 0, 0, 21]
    }
    return keys[key]
