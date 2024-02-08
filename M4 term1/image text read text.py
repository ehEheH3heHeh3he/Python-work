import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Next\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('ATK4.jpg')
text = tess.image_to_string(img)

print(text)