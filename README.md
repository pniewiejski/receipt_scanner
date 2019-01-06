# Receipt scanner

The goal of this project is to create a service which will provide users with the ability to scan receipts and extract data.
It is meant as a tool for better monitoring of  your daily expenses and shopping habbits.

----

## Building blocks
This project was divided into smaller parts:

- [Reader](./documentation/reader.md) - which provides all OCR functionalities. It takes your raw image and outputs formated contents of the receipt.

- [Main Service](./documentation/service.md) - it orchestrates the workflow of the entire application. 

- __React__ client app

<!-- - [Storage](./documentation/storage.md)  -->

----
## How do I run it?
<!-- Well you don't... at this point -->

<!-- ![i](https://i.kym-cdn.com/photos/images/newsfeed/001/305/222/ae7.gif) -->
Start by installing all prerequisites.
### Prerequisites
- Python3 
- Node.js and npm (Node Package Manager)
- Tesseract OCR

### Adding support for other languages in tesseract
Download *.traineddata file from [github.com/tesseract-ocr/tessdata_fast](https://github.com/tesseract-ocr/tessdata_fast). And then place it in your tesseract directory in tessdata/. (eg.: /usr/share/tesseract-ocr/4.00/tessdata)


This project consists of two main parts. If you take a look at the file structure you will notice: `client` and `services`.

```
├── client
├── services
├── documentation
└── uploads

```
Navigate to `client` directory and run following commands:
```
$ npm install 
$ npm start
```
This should install dependencies and start the client app.

Navigate to `services` and run following command (use `pip` if you are on Windows):
```
$ pip3 install -r requirements.txt
```
This will install dependencies listed in `requirements.txt`.

To start backend sevice run: 
```
$ python3 uploader.py
```


**Both client and backend service need to be running!**
