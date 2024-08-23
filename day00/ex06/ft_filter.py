def ft_filter(function, sequence):
    """
    This function filters elements from the given sequence,
    returning only those that satisfy the condition defined
    by the provided function.
    If no function is provided,it returns the elements of the sequence
    that are truthy (i.e., not False, None, 0, or empty).

    Parameters
    ----------
    function (callable): A function that takes a single
    argument and returns True or False.
    If None, the function behaves as if it were the identity function,
    returning only the truthy elements of the sequence.

    sequence (iterable): The sequence to be filtered.

    Return
    ----------
    generator: A generator that yields elements of
    the sequence that pass the filter condition.

    Examples
    ----------
    >>> list(ft_filter(lambda x: x > 0, [1, -2, 3, 0, -5]))
    [1, 3]

    >>> list(ft_filter(None, [0, 1, False, 2, '', 3]))
    [1, 2, 3]
    """
    if function:
        return (x for x in sequence if function(x))
    return (x for x in sequence if x)
