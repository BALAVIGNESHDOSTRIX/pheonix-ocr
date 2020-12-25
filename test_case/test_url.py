from PIL import Image
from urllib.request import urlopen, Request
import io
from pytesseract import image_to_string as imgstr

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = "http://blog.wellcomelibrary.org/wp-content/uploads/2015/12/Archives-OCR-4.jpg"
req = Request(url=url, headers=headers)
fd = urlopen(req)
image_file = io.BytesIO(fd.read())
im = Image.open(image_file)
istr = imgstr(im)
print(istr)

