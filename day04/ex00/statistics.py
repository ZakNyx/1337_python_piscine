from typing import Any, List


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics (mean, median, quartiles, variance, and standard deviation)
    based on the provided *args and **kwargs.

    Args:
        *args: A variable number of numerical values.
        **kwargs: Keyword arguments specifying which statistics to calculate.
                  Possible values: 'mean', 'median', 'quartile', 'var', 'std'.

    Returns:
        None: Prints the requested statistics or 'ERROR' for invalid inputs.
    """
    data: List[float] = [arg for arg in args if isinstance(arg, (int, float))]

    if not data:
        print("ERROR")
        return

    data.sort()

    def mean(data: List[float]) -> float:
        """
        Calculate the mean of the data.
        
        Args:
            data (List[float]): A list of numbers.

        Returns:
            float: The mean of the data.
        """
        if not data:
            print("ERROR")
            return None
        return sum(data) / len(data)

    def median(data: List[float]) -> float:
        """
        Calculate the median of the data.
        
        Args:
            data (List[float]): A sorted list of numbers.

        Returns:
            float: The median of the data.
        """
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        return data[mid]

    def quartiles(data: List[float]) -> List[float]:
        """
        Calculate the first and third quartiles of the data.
        
        Args:
            data (List[float]): A sorted list of numbers.

        Returns:
            List[float]: A list containing the first and third quartiles.
        """
        mid = len(data) // 2
        q1 = median(data[:mid])
        q3 = median(data[mid:]) if len(data) % 2 == 0 else median(data[mid + 1:])
        return [q1, q3]

    def variance(data: List[float], m: float) -> float:
        """
        Calculate the variance of the data.
        
        Args:
            data (List[float]): A list of numbers.
            m (float): The mean of the data.

        Returns:
            float: The variance of the data.
        """
        return sum((x - m) ** 2 for x in data) / len(data)

    def std_dev(var: float) -> float:
        """
        Calculate the standard deviation of the data.
        
        Args:
            var (float): The variance of the data.

        Returns:
            float: The standard deviation of the data.
        """
        return var ** 0.5

    for key, value in kwargs.items():
        if value == "mean":
            m = mean(data)
            if m is not None:
                print(f"mean : {m}")
        elif value == "median":
            med = median(data)
            print(f"median : {med}")
        elif value == "quartile":
            q = quartiles(data)
            print(f"quartile : {q}")
        elif value == "var":
            m = mean(data)
            if m is not None:
                var = variance(data, m)
                print(f"var : {var}")
        elif value == "std":
            m = mean(data)
            if m is not None:
                var = variance(data, m)
                std = std_dev(var)
                print(f"std : {std}")
        else:
            print("ERROR")
