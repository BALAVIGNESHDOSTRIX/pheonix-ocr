#!/usr/bin/env python3
import os
from config import config as conn
import zipfile as zips
import shutil


def isCheckImgfile_Avail(filename):
    file_dir = conn.ROOT + conn.TEMP_IMAGE + conn.ROOT_FLAG + filename
    if os.path.exists(file_dir):
        return True
    return False 

def Str2Txt(filename,string):
    filename = filename.split('.')
    file_dir = conn.ROOT + conn.TEMP_TEXT + conn.ROOT_FLAG + filename[0] + conn.TXT
    with open(file_dir,'w') as filew:
        filew.write(string)
        return True 

def DeleteImageFile(filename):
        file_dir = conn.ROOT + conn.TEMP_IMAGE + conn.ROOT_FLAG + filename
        os.remove(file_dir)
        if isCheckImgfile_Avail(filename):
                return False
        return True

def DeleteTxtFile(filename):
        filenam = filename.split('.')
        file_dir = conn.ROOT + conn.TEMP_TEXT + conn.ROOT_FLAG + filenam[0] + conn.TXT
        os.remove(file_dir)
        if isCheckTxtFile_Avail(filename):
                return False
        return True

def isCheckTxtFile_Avail(filename):
    filename = filename.split('.')
    file_dir = conn.ROOT + conn.TEMP_TEXT + conn.ROOT_FLAG + filename[0] + conn.TXT
    if os.path.exists(file_dir):
        return True,file_dir,filename[0]
    return False 

def isCheckImageZip_Avail(filename):
        file_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG + filename
        if os.path.exists(file_dir):
                return True 
        return False 

def create_Dir(filename):
        filename = filename.split('.')
        file_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG + filename [0]
        maked_dir = os.makedirs(file_dir)
        return True
        

def zip_Extractor(filename):
        split_file = filename.split('.')
        file_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG + filename 
        zip_ref = zips.ZipFile(file_dir, 'r')
        save_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG + split_file[0]
        zip_ref.extractall(save_dir)
        zip_ref.close()
        return True  

def DeleteZipFile(filename):
        file_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG +filename
        os.remove(file_dir)
        if isCheckImageZip_Avail(filename):
                return False 
        return True

def ReturnListZipFile(filename):
        spl_filename = filename.split('.')
        file_dir = conn.ROOT + conn.TEMP_ZIP + conn.ROOT_FLAG + spl_filename[0]
        file_arr = os.listdir(file_dir)
        if file_arr:
                return True,file_arr,file_dir

def ZipTextWriter(string,to_path):
        with open(to_path,'w') as writer:
                writer.write(string)
                return True

def ZipImgsDelete(file_dir):
        os.remove(file_dir)
        return True

def Remove_dir(file_dir):
        shutil.rmtree(file_dir, ignore_errors=True)
        return True

def Dir_Zipper(file_dir,filename):
        filenam = filename.split('.')
        file_target = file_dir + '.' +filenam[1]
        shutil.make_archive(file_dir, 'zip', file_dir)
        if isCheckImageZip_Avail(filename):
                return True,file_target,filenam[0]
        return False




