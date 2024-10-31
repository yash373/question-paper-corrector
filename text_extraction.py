import easyocr

def readText(image:str) -> str:   
    reader = easyocr.Reader(['en'])

    result = reader.readtext(image, detail=1, paragraph=True)

    return (result[0][-1])
