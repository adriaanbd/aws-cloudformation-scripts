import base64
import pytesseract
import cv2


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def ocr(img, oem=None,psm=None, lang=None):
    
    config='--oem {} --psm {} -l {}'.format(oem,psm,lang)

    grey_img = get_grayscale(cv2.imread(img))
    ocr_text = pytesseract.image_to_string(grey_img, config=config)
    
    return ocr_text


def handler(event, context):
    
    # Extract content from json body
    body_image64 = event['image64']
    oem = event["tess-params"]["oem"]
    psm = event["tess-params"]["psm"]
    lang = event["tess-params"]["lang"]
    
    # Decode & save inp image to /tmp
    with open("/tmp/saved_img.png", "wb") as f:
      f.write(base64.b64decode(body_image64))
    
    # Ocr
    ocr_text = ocr("/tmp/saved_img.png",oem=oem,psm=psm,lang=lang)

    return return {
      "ocr": ocr_text,
    }
