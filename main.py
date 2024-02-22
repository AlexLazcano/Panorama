import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    image = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Unable to load image.")
        return

    # cv2.imshow('Image', image)
    # Display the image using Matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")  # Hide axis
    plt.show()

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
