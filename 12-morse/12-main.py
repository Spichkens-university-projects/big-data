morze = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': "...-", 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}


def morse_code(text):
    res = ""
    for char in text:
        if char.lower() in morze:
            res += morze[char.lower()] + " "
        elif char == " ":
            res += "\n"
        else:
            pass

    return res


if __name__ == "__main__":
    print(morse_code("Hello, World"))
