# -*- coding: utf-8 -*-

#Log
log = {
    'active': True,
    'logfile': '/var/log/pheonix_ocr/ocr.log',
    'logrotate': True,
    'log_format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    'maxBytes': 1024 * 1024 * 5, # 5MB
    'backupCount': 5
}

# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
img2str_config = ('--oem 1 --psm 12')

#EXTENSIONS PATH
TEMP_IMAGE = 'temp_images'
TEMP_TEXT = 'temp_text_out'
TEMP_ZIP = 'temp_zip_core'

#ROOTS
ROOT = './'
ROOT_FLAG = '/'

#FILE EXTENSIONS 
TXT = '.txt'
PNG = '.png'
JPG = '.jpg'
JPEG = '.jpeg'
ZIP = '.zip'


