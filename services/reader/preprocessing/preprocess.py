"""
Preprocess images
"""
import cv2

# from utils.crop import crop
# from utils.assertions import assert_area_ratio

from preprocessing.utils.crop import crop
from preprocessing.utils.assertions import assert_area_ratio


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
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    # threshold
    # image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,4)

    return image

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess images before performing OCR")
    parser.add_argument("--image", type=str, required=True, help="Input image path")
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--save", type=str, help="dir path to which output image should be saved")
    args = parser.parse_args()   
    
    # get image
    image = cv2.imread(args.image)
    output = preprocess(image)
    if args.show: 
        cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("output", output)
        cv2.waitKey(0)
    if args.save:
        import os 
        FILE_NAME = os.path.basename(args.image)
        cv2.imwrite(os.path.join(args.save, FILE_NAME), output)
    

