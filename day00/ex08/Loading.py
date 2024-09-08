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
    None
        The function does not return anything, but yields control back to the loop.
    """
    total = len(lst)
    bar_length = 50

    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        percentage = int(percent * 100)

        print(f'{percentage}% |{bar}| {i + 1}/{total}')

        yield item

    print('\n')


def main():
    for item in ft_tqdm(range(333)):
        sleep(0.005)


if __name__ == "__main__":
    main()
