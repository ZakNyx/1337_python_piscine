from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """
    A decorator factory that creates a decorator which limits how many times
    a function can be called.

    Args:
        limit (int): The maximum number of times the decorated function
         can be called.

    Returns:
        Callable: A decorator that will enforce the call limit on the
         decorated function.

    Example:
        >>> @callLimit(3)
        ... def my_function():
        ...     print("Function called")
        ...
        >>> my_function()  # Function called
        >>> my_function()  # Function called
        >>> my_function()  # Function called
        >>> my_function()  # ERROR: You have
         called <function_name> too many times!
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
        A decorator that wraps the given function and enforces the call limit.

        Args:
            function (Callable): The function to be decorated.

        Returns:
            Callable: The decorated function with the call limit applied.

        Raises:
            AssertionError: If the function is called more times than
             allowed by `limit`.

        Example:
            >>> @callLimit(2)
            ... def my_function():
            ...     print("Function called")
            ...
            >>> my_function()  # Function called
            >>> my_function()  # Function called
            >>> my_function()  # ERROR: You have called
             <function_name> too many times!
        """
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            The inner function that tracks the number of times the decorated
             function is called and raises an error if the limit is exceeded.

            Args:
                *args: Positional arguments passed to the original function.
                **kwds: Keyword arguments passed to the original function.

            Returns:
                Any: The return value of the original function if the call
                 limit is not exceeded.

            Raises:
                AssertionError: If the function is called more than the
                 specified limit.
            """
            nonlocal count
            count += 1
            try:
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(
                        f"Error: You have called {function.__name__} "
                        f"too many times!"
                    )
            except AssertionError as error:
                print(f"ERROR: {error}")

        return limit_function

    return callLimiter
