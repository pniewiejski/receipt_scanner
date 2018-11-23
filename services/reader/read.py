import cv2

from preprocessing.preprocess import preprocess
from ocr.ocr_google import ocr
from parsing.parser import parse

def read(path: str):
    """
    `path` to image file

    Errors
    ------
    
    IOError is raised when no image can be found under `path`.
    """
    image = cv2.imread(path) # image is None if no image is found/ opened
    if image is None:
        raise IOError("Could not open image file under: {}".format(path))

    image = preprocess(image) 
    cv2.imwrite(path, image)
    text = ocr(path)
    receipt = parse(text)
    return receipt

# if __name__ == "__main__":
#     json = read('./test_images/iphone2.jpg')
#     print(json)
