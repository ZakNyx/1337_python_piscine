class Calculator:
    """
    A calculator class that performs vector operations including dot product,
    vector addition, and vector subtraction. All operations assume the vectors
    are of equal length and handle float values.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the result of the dot product.

        Example:
            V1 = [1.0, 2.0, 3.0]
            V2 = [4.0, 5.0, 6.0]
            Dot product is: 32.0
        """
        result = 0
        for i, v1 in enumerate(V1):
            result += v1 * V2[i]
        print(f"Dot Product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector with one decimal point formatting.

        Example:
            V1 = [1.0, 2.0, 3.0]
            V2 = [4.0, 5.0, 6.0]
            Add Vector is: ['5.0', '7.0', '9.0']
        """
        result = []
        for i, v1 in enumerate(V1):
            result.append(v1 + V2[i])
        formatted_result = [f"{x:.1f}" for x in result]
        print(f"Add Vector is: {formatted_result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first vector element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None: Prints the resulting vector with one decimal point formatting.

        Example:
            V1 = [5.0, 6.0, 7.0]
            V2 = [2.0, 4.0, 6.0]
            Sous Vector is: ['3.0', '2.0', '1.0']
        """
        result = []
        for i, v1 in enumerate(V1):
            result.append(v1 - V2[i])
        formatted_result = [f"{x:.1f}" for x in result]
        print(f"Sous Vector is: {formatted_result}")

