def te_ach(error_str):
    keyboard_corr_dict = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "w": "q", "e": "w", "r": "e", "t": "r", "y": "t", "u": "y", "i": "u", "o": "i", "p": "o", "[": "p", "]": "[", "\\": "]",
        "s": "a", "d": "s", "f": "d", "g": "f", "h": "g", "j": "h", "k": "j", "l": "k", ";": "l", "'": ";",
        "x": "z", "c": "x", "v": "c", "b": "v", "n": "b", "m": "n", ",": "m", ".": ",", "/": ".", " ": " "
    }
    return keyboard_corr_dict[error_str.lower()].upper()

def process_input(input_str):
    corrected_str = ""
    for type_word in input_str:
        corrected_str += te_ach(type_word)
    return corrected_str

def main():
    try:
        while True:
            input_str = input()
            print(process_input(input_str))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
