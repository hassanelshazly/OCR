from base64 import b64encode
import json
import sys
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
api_key = "AIzaSyBR-_VqcK-BPIrGTVJjmMGTx8r3gF0D-b4"
imgname = "example_01.jpg"

def main():
    if len(sys.argv) == 2:
	    imgname = sys.argv[1]
    response = request_ocr(api_key, imgname)
    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
    else:
        resp = response.json()['responses'] 
        t = resp['textAnnotations'][0]
        # print("    Bounding Polygon:")
        # print(t['boundingPoly'])
        print("Text:")
        print(t['description'])


def make_image_data(imgname):
    """Returns the image data as bytes"""
    with open(imgname, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        imgdict = ({
                'image': {'content': ctxt},
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1
                }]
        })
    return json.dumps({"requests": imgdict }).encode()

def request_ocr(api_key, imgname):
    response = requests.post(ENDPOINT_URL,
                             data=make_image_data(imgname),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})
    return response

if __name__ == '__main__':
    main()
