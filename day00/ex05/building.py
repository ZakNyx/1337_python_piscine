import sys


def breakdown_text(text: any):
    """
    This function displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces.

    Parameters
    ----------
    text (input): text that will be analised

    Prints
    ----------
    Number of characters
    Number of upper case letters
    Number of lower case letters
    Number of ponctuation marks
    Number of spaces
    Number of digits

    Return
    ----------
    None
    """
    n_char = len(text)
    n_upper = 0
    n_lower = 0
    n_ponc = 0
    n_space = 0
    n_digit = 0
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in text:
        if char.isupper():
            n_upper += 1
        elif char.islower():
            n_lower += 1
        elif char in punctuation:
            n_ponc += 1
        elif char.isspace():
            n_space += 1
        elif char.isdigit():
            n_digit += 1
    print(f"The text contains {n_char} characters:")
    print(f"{n_upper} upper letters")
    print(f"{n_lower} lower letters")
    print(f"{n_ponc} punctuation marks")
    print(f"{n_space} spaces")
    print(f"{n_digit} digits")


def main():
    """
    Main function to execute the text analysis program.

    This function checks the number of command-line arguments. If more than one argument is provided, 
    it raises an AssertionError. If no arguments are provided, it prompts the user to input a text string.
    It then passes the text string to the breakdown_text function for analysis.

    If an AssertionError is raised due to incorrect usage, the error message is printed.

    Returns
    -------
    None
    """
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("Too many arguments!")
        elif len(sys.argv) == 1:
            try:
                text = input("Please enter the text you want to analyse\n")
                text += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        breakdown_text(text)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
