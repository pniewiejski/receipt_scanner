# Reader - *OCR and stuff*

Reader is meant to take an input image (eg. photo taken with a smartphone) and output formated contents of the scanned receipt. To achieve this goal it goes through the following steps:

### Image preprocessing 
To help OCR module and increase its accuracy module we preprocess images. 
- [ ] **Rescaling** - Tesseract works best when the image is at least 300 dpi.
- [ ] **Blurring** -  is used in order to reduce noise.
- [ ] **Thersholding** 
- [x] **Crop** - *"cut out"* the receipt from original image

### Optical Character Recognition
For OCR we are using [tesseract](https://github.com/tesseract-ocr/tesseract) and [pytesseract](https://github.com/madmaze/pytesseract).

### Parsing string data according to a selected parsing strategy
The problem with parsing contents of receipts is that every store have different receipt layout. Because of that we had to create different parsing strategies for different layouts.


### Formating data into a standardised form.

