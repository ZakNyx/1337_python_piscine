import sys
from time import sleep

def ft_tqdm(lst: range) -> None:
    """
    A simple implementation of a progress bar that iterates over a given range and yields items.

    Parameters
    ----------
    lst : range
        The range to iterate over.

    Yields
    ------
    Any
        The current item in the range.
    """
    total = len(lst)
    bar_length = 50

    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        percentage = percent * 100

        sys.stdout.write(f'\r{int(percentage)}% |{bar}| {i + 1}/{total}\n')
        sys.stdout.flush()

        yield item

    sys.stdout.write('\n')
    sys.stdout.flush()


def main():
    for item in ft_tqdm(range(333)):
        pass
        sleep(0.005)


if __name__ == "__main__":
    main()

