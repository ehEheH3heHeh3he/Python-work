from xml.etree.ElementInclude import include



fileName = 'MyDoc.pdf'
documentTitle = 'Document title!'
title = 'ATK CHECK LIST'

textLines = [
'No.1 Thanakrit',
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
