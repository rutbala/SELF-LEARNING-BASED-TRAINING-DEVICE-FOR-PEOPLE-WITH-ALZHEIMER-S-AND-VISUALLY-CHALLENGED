from  PIL import  Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
img_path='Samples/test.png'
text=pytesseract.image_to_string(Image.open(img_path), config=tessdata_dir_config)
 
print(text)
