"""
Main OCR module
"""
import pytesseract

def ocr(image, language="eng") -> str:
    """
    Main OCR routine. 

    `image` - openCV or Pillow image

    `language` - string representing tesserect language, eg. 'pol' or 'eng'
    """
    text = pytesseract.image_to_string(image, lang=language) 
    # TODO: implement case where there's no 'pol' file

    return text

if __name__ == "__main__": 
    import sys
    import cv2
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else: 
        path = "./test/test_images/test.JPG"
    img = cv2.imread(path)
    text = ocr(img, language="pol")
    print(text)
