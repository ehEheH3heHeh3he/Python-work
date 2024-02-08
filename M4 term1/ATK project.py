from xml.etree.ElementInclude import include
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Next\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('ATK4.jpg')
text = tess.image_to_string(img)

print(text)


fileName = 'MyDoc.pdf'
documentTitle = 'Document title!'
title = 'ATK CHECK LIST'

textLines = [
'No.1 : ',text,
'No.2',
'No.3'
]


from reportlab.pdfgen import canvas 

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

pdf.drawCentredString(290,800,title)
text = pdf.beginText(40,750)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)


pdf.save()