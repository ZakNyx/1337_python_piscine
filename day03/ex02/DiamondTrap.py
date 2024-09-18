from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class that inherits from Baratheon and Lannister.

    This class models a king with attributes for eyes and hair color, and inherits
    properties and methods from Baratheon and Lannister families.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize the King object.

        Args:
            first_name (str): The first name of the king.
            is_alive (bool, optional): The alive status of the king. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Set the eye color of the king.

        Args:
            color (str): The color of the king's eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the king.

        Args:
            color (str): The color of the king's hair.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the eye color of the king.

        Returns:
            str: The color of the king's eyes.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the king.

        Returns:
            str: The color of the king's hair.
        """
        return self.hairs
