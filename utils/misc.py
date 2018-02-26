import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract-OCR/tesseract'

def ocr(img):
    ret = pytesseract.image_to_string(Image.fromarray(img))
    return ret