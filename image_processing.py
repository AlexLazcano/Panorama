import numpy as np
import cv2
import matplotlib.pyplot as plt

def print_matrix(matrix):
    for row in matrix:
        print(row)
    


def fast_detector(image, h, w, t):

    rad = 4
    endh = h - rad
    endw = w - rad

    pRes = np.zeros((h, w), dtype=np.int8)

    tR = np.identity(3, dtype=np.int8)
    tR[0, 2] = 3

    tL = np.identity(3, dtype=np.int8)
    tL[0, 2] = -3

    tD = np.identity(3, dtype=np.int8)
    tD[1, 2] = 3

    tU = np.identity(3, dtype=np.int8)
    tU[1, 2] = -3

    tU1 = np.identity(3, dtype=np.int8)
    tU1[1, 2] = -1

    tD1 = np.identity(3, dtype=np.int8)
    tD1[1, 2] = 1

    tL1 = np.identity(3, dtype=np.int8)
    tL1[0, 2] = -1

    tR1 = np.identity(3, dtype=np.int8)
    tR1[0, 2] = 1

    center = np.array([rad, rad, 1])

    p1 = tU
    p2 = tU @ tR1
    p3 = np.array([[1,0,2], [1,0,-2], [0,0,1]])
    p4 = tR @ tU1
    p5 = tR 
    p6 = tR @ tD1  # check 
    p7 = np.array([[1,0,2], [1,0,2], [0,0,1]]) 
    p8 = tD @ tR1
    p9 = tD
    p10 = tD @ tL1
    p11 = np.array([[1,0,-2], [1,0,2], [0,0,1]])
    p12 = tL @ tD1
    p13 = tL
    p14 = tL @ tU1
    p15 = np.array([[1,0,-2], [1,0,-2], [0,0,1]])
    p16 = tU @ tL1

    transformArrays = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

    # print("transformArrays: ", transformArrays)



    print("image: ", image.shape)

    for c in range(rad, endw):
        for r in range(rad, endh):

            image[center[0], center[1]] = 255

            m = image[c - rad : c + rad + 1, r - rad : r + rad + 1]

            for transform in transformArrays: 

                transformed = transform @ center 

                # print_matrix(transform)

                # print("x y: ", transformed[0], transformed[1])
                # print()

                m[transformed[0], transformed[1]] = 255
                

    
    print("m: ", m.shape)
    plt.imshow(m, cmap="gray")
    plt.show()
            


def createAndSaveRandomImage(h, w):
    image = np.random.rand(h, w)

    scaled = (image * 255).astype(np.uint8)
    cv2.imwrite("images/random.png", scaled)

def createAndSaveBlackImage(h, w):
    image = np.zeros((h, w), dtype=np.uint8)
    cv2.imwrite("images/black.png", image)