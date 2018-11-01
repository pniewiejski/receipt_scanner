"""
Preprocess images
"""
import argparse
import cv2

from utils.crop import crop
from utils.assertions import assert_area_ratio

def preprocess(image):
    """
    Returns `image` after preprocessing
    """
    # try to crop
    cropped = crop(image)
    if cropped is not None:
        # assert crop quality
        if assert_area_ratio(image, cropped):
            image = cropped
    # filter
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold

    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess images before performing OCR")
    parser.add_argument("--image", type=str, required=True, help="Input image path")
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()   
    
    # get image
    image = cv2.imread(args.image)
    output = preprocess(image)
    if args.show: 
        cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("output", output)
        cv2.waitKey(0)

    

