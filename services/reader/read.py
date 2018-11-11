"""

"""
import cv2

from preprocessing.preprocess import preprocess
from ocr.ocr import ocr
from parsing.parser import parse

def read(path: str):
    """
    `path` to image file
    """
    image = cv2.imread(path)
    
    # cv2.imshow("original", image)
    # cv2.waitKey(0)

    image = preprocess(image)

    # cv2.imshow("processed", image)
    # cv2.waitKey(0)

    text = ocr(image)

    # print(text)

    receipt = parse(text)

    return receipt

# if __name__ == "__main__":
#     json = read('../test_images/3.png')
#     print(json)
