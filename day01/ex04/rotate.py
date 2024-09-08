from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array: np.array, x: int, y: int, width: int,
         height: int, depth: int = 3) -> np.array:
    return array[y: y + height, x: x + width, :depth]


def transpose_image(image: np.array) -> np.array:
    height, width, depth = image.shape
    transposed_image = np.zeros((width, height, depth), dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            transposed_image[j, i] = image[i, j]
    return transposed_image


def main():
    try:
        image = ft_load("animal.jpeg")
    except Exception as e:
        print(f'Error loading image {e}')
        exit()

    image_trimmed = trim(image, 450, 100, 400, 400, 1)

    print(f"The shape of the image is: {image_trimmed.shape} or "
          f"({image_trimmed.shape[0]}, {image_trimmed.shape[1]})")
    print(image_trimmed)
    image_transposed = transpose_image(image_trimmed)
    print(f"New shape after Transpose: "
          f"({image_transposed.shape[0]}, {image_transposed.shape[1]})")
    print(image_transposed)

    image_gray = np.squeeze(image_transposed)
    plt.imshow(image_gray, cmap='gray')
    plt.colorbar()  # Adds a color scale to the right of the image
    plt.xlabel('Width (pixels)')  # X-axis label
    plt.ylabel('Height (pixels)')  # Y-axis label
    plt.title('Rotated Grayscale Image')  # Title of the plot
    plt.show()


if __name__ == "__main__":
    main()
