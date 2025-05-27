MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "  ",
}


MORSE_CODE_DICT_REVERSE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "--..--": ",",
    ".-.-.-": ".",
    "..--..": "?",
    "-..-.": "/",
    "-....-": "-",
    "-.--.": "(",
    "-.--.-": ")",
    "    ": " ",
    "": " ",
}


def message_to_morse(message):
    morse = ""
    error_message = ""
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + " "
        else:
            error_message += f"Can't convert char [{char}]"
            break
    if error_message:
        print(error_message)
    else:
        print(morse)


def morse_to_message(message):
    morse_translated = ""
    error_message = ""
    words = message.split("    ")
    for word in words:
        codes = word.split()
        for code in codes:
            if code in MORSE_CODE_DICT_REVERSE:
                morse_translated += MORSE_CODE_DICT_REVERSE[code]
            else:
                error_message += f"Can't convert code [{code}] "
        morse_translated += " "
    if error_message:
        print(error_message)
    else:
        print(morse_translated.capitalize())


def translate_text(message):
    # ChatGPT'ed, I couldn't make up the logic myself.
    if all(char in ".- " for char in message):
        morse_to_message(message)
    else:
        message_to_morse(message)


if __name__ == "__main__":
    translate_text(input(""))
