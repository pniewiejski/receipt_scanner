"""
Main OCR module
"""
import pytesseract

def ocr(image) -> str:
    """
    Main OCR routine. 

    `image` - openCV or Pillow image
    """
    text = pytesseract.image_to_string(image, lang="pol") 
    # TODO: implement case where there's no 'pol' file

    return text

# if __name__ == "__main__": 
#     import cv2
#     img = cv2.imread('/home/piotr/Desktop/test2.jpeg')
#     text = ocr(img)
#     print(text)
