"""
Main OCR module
"""
import pytesseract

def ocr(image) -> str:
    """
    Main OCR routine. 

    `image` - openCV or Pillow image
    """
    text = pytesseract.image_to_string(image)

    return text

if __name__ == "__main__": 
    import cv2
    img = cv2.imread('../../test_images/2.jpg')
    text = ocr(img)
    print(text)