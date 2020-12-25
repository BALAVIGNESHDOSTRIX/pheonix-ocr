#!/usr/bin/env python3

from pytesseract import image_to_string as imgstr
from PIL import Image 
from config import config as conn 
from file_handlers import file_helper as filehelp
import cv2
from urllib.request import urlopen, Request
import io
import requests

headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }       

def Img2Str(filename):
        file_dir = conn.ROOT + conn.TEMP_IMAGE + conn.ROOT_FLAG + filename
        img = cv2.imread(file_dir,cv2.IMREAD_COLOR)
        string = imgstr(img, config = conn.img2str_config)
        if string:
                return True,string
        return False


def ZipImg2Str(file_arr,file_dir):
        arr_length = len(file_arr)
        index = 0
        for imgfile in file_arr:
                file_path = file_dir + conn.ROOT_FLAG + imgfile
                string = imgstr(Image.open(file_path))
                tempfile_spl = imgfile.split('.')
                topath = file_dir + conn.ROOT_FLAG + tempfile_spl[0]
                if filehelp.ZipTextWriter(string,topath):
                        if filehelp.ZipImgsDelete(file_path):
                                index = index + 1
        
        if arr_length == index:
                return True

def Url2Str(url):
        req = Request(url=url, headers=headers)
        fd = urlopen(req)
        # image_file = io.BytesIO(fd.read())
        im_obj = Image.open(fd)
        istr = imgstr(im_obj, config = conn.img2str_config)
        return istr





