import re
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import requests
import csv


url = r'https://link.amazonaws.com/com.link.fileservice/files/documents/file_link.jpg'
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image, lang='eng')
print(text)

# Finds date formats '01/01/2020' | '01.01.2020' | '01 Jan 2020' | '01 January 2020' | 'January 01 2020'

pattern = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(20)\d\d|'
                     r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012]).(20)\d\d|'
                     r'(0[1-9]|[12][0-9]|3[01])\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
                     r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\s(20)\d\d|'
                     r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
                     r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\s(0[1-9]|[12][0-9]|3[01])\s(20)\d\d')

x = re.findall(pattern, text)
print(x)
