"""
This OCR module employs google vision API
"""
import requests
import json
import base64

def ocr(image_path):
    encoded_image = encode_image(image_path)
    payload = {
        "requests":[
            {
            "image":{"content":encoded_image},
            "features":[{"type":"DOCUMENT_TEXT_DETECTION", "maxResults":1}],
            "imageContext": {"languageHints": ["pl"]}
            }]}
    payload = json.dumps(payload)
    api_key = get_api_key()
    response = requests.post("https://vision.googleapis.com/v1/images:annotate?key="+api_key, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        text = data["responses"][0]["textAnnotations"][0]["description"]
        return text
    else: 
        raise Exception("Google Vision API status code: {}".format(response.status_code))

def encode_image(image_path) -> str:
    """
    Encodes image to base64 and returns a python 3 str representation 
    (so it can be serialized to JSON)
    """
    with open(image_path, "rb") as image_file:
        data = image_file.read() # read image - data is bytes
        data = base64.b64encode(data) # base64 - data is bytes
        data = data.decode("utf-8") # decode bytes to str 
    return data

def get_api_key() -> str:
    with open("../../../api_key.json") as f:
        api_key = json.load(f)
    return api_key["apiKey"]

if __name__ == "__main__":

    test3 = ocr("../test_images/test3.png")
    print(test3)        