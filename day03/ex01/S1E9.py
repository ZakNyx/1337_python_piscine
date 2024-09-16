from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class for characters.

    Attributes:
    - first_name (str): The first name of the character.
    - is_alive (bool): The status of the character, True if alive, False if dead.
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character.

        Parameters:
        - first_name (str): The first name of the character.
        - is_alive (bool, optional): The living status of the character, default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Marks the character as dead.

        This method should be overridden by subclasses.
        """
        pass


class Stark(Character):
    """
    A class representing a Stark character, subclass of Character.

    Attributes:
    - first_name (str): The first name of the Stark character.
    - is_alive (bool): The status of the character, True if alive, False if dead.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Stark character.

        Parameters:
        - first_name (str): The first name of the Stark character.
        - is_alive (bool, optional): The living status of the character, default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Marks the Stark character as dead by setting is_alive to False.
        """
        self.is_alive = False
