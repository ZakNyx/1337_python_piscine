import sys


def strToMorse(text):
    NESTED_MORS = {
         'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--', 'N': '-.',
         'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...',
         'T': '-', 'U': '..-', 'V': '...-',
         'W': '.--', 'X': '-..-', 'Y': '-.--',
         'Z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', ' ': '/',
         }
    result = []
    for char in text.upper():
        if char in NESTED_MORS:
            result.append(NESTED_MORS[char])
        else:
            raise AssertionError(f"This char is not supported {char}")
        return ' '.join(result)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Too Many Arguments!")
        output = strToMorse(sys.argv[1])
        print(output)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
