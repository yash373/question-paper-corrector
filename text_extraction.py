import easyocr
from imgurpython import ImgurClient
from dotenv import load_dotenv

load_dotenv('.env.local')

def upload_image(path:str) -> None:
    client = ImgurClient("cb30ede881b8f55","7b67ef91de5555e1ce8929f13cac909b8e1dfaf6")
    # Upload the image
    uploaded_image = client.upload_from_path(path, anon=True)
    # Return the URL of the uploaded image
    return uploaded_image['link']

def readText(image:str) -> str:   
    reader = easyocr.Reader(['en'])

    result = reader.readtext(image, detail=1, paragraph=True)

    return (result[0][-1])