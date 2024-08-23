def count_in_list(lst, item) -> int:
    """
    Count the occurrences of a specific item in a list.

    Parameters
    ----------
    lst : list
        The list in which to count the occurrences of the item.
    item : any
        The item to count within the list.

    Returns
    -------
    int
        The number of times the item appears in the list.

    """
    return lst.count(item)


def main():
    lst = [1, 2, 2, 3, 4, 2]
    item = 2
    count = count_in_list(lst, item)
    print(f'The item {item} appears {count} times in the list {lst}.')


if __name__ == "__main__":
    main()
