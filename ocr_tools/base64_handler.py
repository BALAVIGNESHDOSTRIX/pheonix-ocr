from base64 import decodestring

def WrireBase64ToImg(filename,base64, folder):
    dir = folder + '/' + filename
    with open(dir,"wb") as f: 
        f.write(decodestring(base64))
