import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('test1.png', detail = 1)

print(result)