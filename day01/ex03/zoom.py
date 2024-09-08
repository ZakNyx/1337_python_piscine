from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array: np.array, x: int, y: int, width: int,
         height: int, depth: int = 3) -> np.array:
    """
    Trims a 3D image array (height x width x channels)

    Parameters:
    - array: The image array to be trimmed.
    - x: The x-coordinate of the top-left corner of the trimming box.
    - y: The y-coordinate of the top-left corner of the trimming box.
    - width: The width of the trimming box.
    - height: The height of the trimming box.
    - depth: The number of channels to retain (default is 3 for RGB images).

    Returns:
    - A trimmed array with the specified dimensions.
    """
    return array[y: y + height, x: x + width, :depth]


def main():
    """
    Loads an image, trims it, converts it to grayscale if required,
    and displays the result along with the image's shape information.
    """
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(f"Error loading image: {e}")
        exit()

    print(f'The shape of the image is: {image.shape}')
    print(image)

    # Trim the image
    image_trimmed = trim(image, 450, 100, 400, 400, 1)
    print(f'New shape after slicing: {image_trimmed.shape} or '
          f'({image_trimmed.shape[0]}, {image_trimmed.shape[1]})')
    print(image_trimmed)

    # Display the trimmed image in grayscale with axes and color scale
    image_gray = np.squeeze(image_trimmed)
    plt.imshow(image_gray, cmap='gray')
    plt.colorbar()  # Adds a color scale to the right of the image
    plt.xlabel('Width (pixels)')  # X-axis label
    plt.ylabel('Height (pixels)')  # Y-axis label
    plt.title('Trimmed Grayscale Image')  # Title of the plot
    plt.show()


if __name__ == "__main__":
    main()
