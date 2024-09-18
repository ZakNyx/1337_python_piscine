from S1E9 import Character


class Baratheon(Character):
    """
    A class representing the Baratheon family, inheriting from the Character class.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Whether the character is alive. Default is True.
        family_name (str): The family name of the character, default is 'Baratheon'.
        eyes (str): The eye color of the character, default is 'Brown'.
        hairs (str): The hair color of the character, default is 'Dark'.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon character.

        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool, optional): The living status of the character. Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "Dark"

    def die(self):
        """Marks the character as dead by setting is_alive to False."""
        self.is_alive = False


class Lannister(Character):
    """
    A class representing the Lannister family, inheriting from the Character class.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Whether the character is alive. Default is True.
        family_name (str): The family name of the character, default is 'Lannister'.
        eyes (str): The eye color of the character, default is 'Blue'.
        hairs (str): The hair color of the character, default is 'Light'.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Lannister character.

        Parameters:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): The living status of the character. Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "Light"

    def die(self):
        """Marks the character as dead by setting is_alive to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a new Lannister character.

        Parameters:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): The living status of the character. Default is True.

        Returns:
            Lannister: A new instance of the Lannister class with the specified name and is_alive status.
        """
        inst = cls(first_name, is_alive)
        return inst
