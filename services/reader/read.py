import cv2

from preprocessing.preprocess import preprocess
from ocr import ocr
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
    text = ocr(image, language="pol")
    print(text)
    receipt = parse(text)
    return receipt

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else: 
        path = "./test/test_images/test.JPG"
    json = read(path)
    print(json)
