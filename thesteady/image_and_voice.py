import pytesseract
from google.cloud import speech
import requests
from PIL import Image
from io import BytesIO


def parse_image(image_url):
    r = requests.get(image_url)
    img = Image.open(BytesIO(r.content))
    text = pytesseract.image_to_string(img, lang='eng')
    return text



def parse_voice(voice_url):
    # For demo purposes, just acknowledge the voice message
    return "I see you've sent an audio message. For now, I'll treat it as if you sent 'EARN 500'."
