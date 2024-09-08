from PIL import Image
import os
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image from the specified path and returns it as a NumPy array.

    This function checks whether the provided path exists and
    whether the file has the correct extension (.jpeg or .jpg).
    If these conditions are not met,
    it raises an AssertionError and prints an error message.

    Parameters
    ----------
    path : str
        The file path to the image.

    Returns
    -------
    np.array
        The image loaded as a NumPy array. The array will have dimensions
        corresponding to the height, width, and number of layers (channels)
        in the image.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("Wrong path: File not found")
        if not path.lower().endswith(("jpeg", "jpg")):
            raise AssertionError("Wrong extention only JPG, JPEG allowed")
        img = Image.open(path)
        img = np.asarray(img)
        return img
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return ""
