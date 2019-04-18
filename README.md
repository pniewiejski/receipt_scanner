# Receipt scanner

School project for scanning printed text (receipts).

## Building blocks
### Reader - *OCR and stuff*

Reader is meant to take an input image (eg. photo taken with a smartphone) and output 
formated contents of the scanned receipt. To achieve this goal it goes through 
the following steps:

## Image preprocessing 
To help OCR module and increase its accuracy module we preprocess images. 
- [x] **Crop** - *"cut out"* the receipt from original image
- [ ] **Rescaling** - Tesseract works best when the image is at least 300 dpi.
- [x] **Blurring** -  is used in order to reduce noise.
- [x] **Thersholding** 

Cropping works best when receipt is visible in its entirety (all four corners of the paper sheet have to be visible). It's best practice for pictures to have a dark, uniform background. Otherwise there might be problems detecting your receit.

## Optical Character Recognition
For OCR we are using [tesseract](https://github.com/tesseract-ocr/tesseract) and [pytesseract](https://github.com/madmaze/pytesseract).

## Parsing string data according to a selected parsing strategy
The problem with parsing contents of receipts is that every store have different receipt layout. Because of that we had to create different parsing strategies for different layouts.


----
## How do I run it?
Well you don't... at this point

![i](https://i.kym-cdn.com/photos/images/newsfeed/001/305/222/ae7.gif)

### Adding support for other languages in tesseract

Download `*.traineddata` file from [github.com/tesseract-ocr/tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast). 
Then place it in your tesseract directory in `tessdata/`. (eg.: `/usr/share/tesseract-ocr/4.00/tessdata`)
