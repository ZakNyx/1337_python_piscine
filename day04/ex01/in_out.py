def square(x: int | float) -> int | float:
    """
    Function to return the square of x.
    ----------
    Args:
        x (int | float): The number to be squared.
    ----------
    Returns:
        int | float: The square of x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Function to return the exponentiation of x by itself (x ** x).
    ----------
    Args:
        x (int | float): The number to be raised to the power of itself.
    ----------
    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Outer function that accepts a value x and a function.
    It returns an inner function that computes a result
     based on x and the passed function.
    ----------
    Args:
        x (int | float): The value to be processed.
        function (Callable): A function to apply on x (e.g., square or pow).
    ----------
    Returns:
        Callable: An inner function that, when called,
         returns the result of applying the function on x.
    """
    count = 0  # Keep track of how many times inner function is called
    result = x  # Initialize result with x

    def inner() -> float:
        """
        Inner function that applies the passed function
         on x and increments the count.
        ----------
        Returns:
            int | float: The result of
             applying the passed function on x.
        """
        nonlocal count, result
        count += 1
        result = function(result)  # Apply function on the last result
        print(f"Inner function called {count} time(s). Result: {result}")
        return result

    return inner

    return inner
