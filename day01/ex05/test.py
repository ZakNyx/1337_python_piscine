import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def display_image(array):
    array = np.squeeze(array)
    plt.imshow(array, cmap='gray')
    plt.axis('off')
    plt.show()


def main():
    """
        Open the image and display it with differents color filters
    """

    try:
        image = ft_load('landscape.jpg')
    except Exception as e:
        print(e)
        exit()

    print(f'The shape of the image is: {image.shape}')
    print(image)

    display_image(image)

    display_image(ft_invert(image))
    display_image(ft_red(image))
    display_image(ft_green(image))
    display_image(ft_blue(image))
    display_image(ft_grey(image))


if __name__ == "__main__":
    main()
