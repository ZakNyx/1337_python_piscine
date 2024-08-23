import sys
from ft_filter import ft_filter


def main():
    """
    Parameters
    ----------
    S: String
    N: Integer

    Return
    ----------
    Prints a list of words from S that have a length greater than N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Two Arguments Only: "
                                 "a string and an integer")
        str = sys.argv[1]

        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Second argument should "
                                 "be an integer.")
        n = int(sys.argv[2])
        result = list(ft_filter(lambda wrd: len(wrd) > n, str.split()))

        print(result)
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except ValueError as error:
        print(f"ValueError: {error}")


if __name__ == "__main__":
    main()
