import os
import pytesseract

# Set the path for the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'
from PIL import Image

# Load an image using PIL
image_path = '10001.png'  # Make sure this is the correct path to your image
pil_image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(pil_image)
print(text)
