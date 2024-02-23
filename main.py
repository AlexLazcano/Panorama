import cv2
import numpy as np
from matplotlib import pyplot as plt

from image_processing import fast_detector, createAndSaveRandomImage, createAndSaveBlackImage


def main():
    img_paths = ["images/img1.jpg", "images/img2.jpg"]

    # images_bw = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in img_paths]

    # for image in images_bw:
    #     plt.figure()
    #     plt.imshow(image, cmap="gray")
    #     plt.axis("off")
    #     plt.show()

    # generate 8x8 image
    h, w = 9, 9

    # createAndSaveRandomImage(h, w)
    createAndSaveBlackImage(h, w)

    image = cv2.imread("images/black.png", cv2.IMREAD_GRAYSCALE)
    print(image)
    

    plt.figure()
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    # dont stop the program
    plt.show(block=False)

    fast_detector(image=image, h=h, w=w, t=0.5)


if __name__ == "__main__":
    main()
