import numpy as np


def ft_invert(array: np.array) -> np.array:
    """
    Modifies the input image array to make the image colors inverted.

    Parameters:
    image_array (np.ndarray): Input RGB image array.

    Returns:
    np.ndarray: Image array with only the red channel preserved.
    """
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a NumPy array")
    inverted_array = 255 - array
    return inverted_array


def ft_red(image_array: np.array) -> np.array:
    """
    Modifies the input image array to make the image predominantly red.

    Parameters:
    image_array (np.ndarray): Input RGB image array.

    Returns:
    np.ndarray: Image array with only the red channel preserved.
    """
    # Ensure the input is a valid NumPy array
    if not isinstance(image_array, np.ndarray):
        raise ValueError("Input must be a NumPy array")

    # Copy the image array to avoid modifying the original
    red_image_array = image_array.copy()

    # Set the Green and Blue channels to 0
    red_image_array[..., 1] = 0  # Set Green channel to 0
    red_image_array[..., 2] = 0  # Set Blue channel to 0

    return red_image_array


def ft_green(image_array: np.array) -> np.array:
    """
    Modifies the input image array to make the image predominantly green.

    Parameters:
    image_array (np.ndarray): Input RGB image array.

    Returns:
    np.ndarray: Image array with only the green channel preserved.
    """
    # Ensure the input is a valid NumPy array
    if not isinstance(image_array, np.ndarray):
        raise ValueError("Input must be a NumPy array")

    # Copy the image array to avoid modifying the original
    red_image_array = image_array.copy()

    # Set the Green and Blue channels to 0
    red_image_array[..., 0] = 0  # Set Red channel to 0
    red_image_array[..., 2] = 0  # Set Blue channel to 0

    return red_image_array


def ft_blue(image_array: np.array) -> np.array:
    """
    Modifies the input image array to make the image predominantly blue.

    Parameters:
    image_array (np.ndarray): Input RGB image array.

    Returns:
    np.ndarray: Image array with only the blue channel preserved.
    """
    # Ensure the input is a valid NumPy array
    if not isinstance(image_array, np.ndarray):
        raise ValueError("Input must be a NumPy array")

    # Copy the image array to avoid modifying the original
    red_image_array = image_array.copy()

    # Set the blue and Blue channels to 0
    red_image_array[..., 0] = 0  # Set Red channel to 0
    red_image_array[..., 1] = 0  # Set Green channel to 0

    return red_image_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the input image array to grayscale using simple averaging.

    Parameters:
    array (np.ndarray): Input RGB image array.

    Returns:
    np.ndarray: Grayscale image array with 3 channels (RGB).
    """

    # Compute the grayscale value by averaging the RGB channels
    grey_array = np.mean(array, axis=2, keepdims=True)

    # Convert the grayscale image array to 3 channels (RGB)
    grey_image_array = np.repeat(grey_array, 3, axis=2).astype(array.dtype)

    return grey_image_array
