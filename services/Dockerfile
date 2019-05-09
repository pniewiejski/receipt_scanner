FROM python:3

WORKDIR /usr/apps/receipt_scanner

RUN apt-get update \
    && apt-get install -y tesseract-ocr

ADD https://github.com/tesseract-ocr/tessdata/raw/master/pol.traineddata /usr/share/tesseract-ocr/tessdata

COPY . .

RUN pip3 install -r requirements.txt

CMD ["make", "run"]