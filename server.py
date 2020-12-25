from flask import Flask,send_file,Response, redirect, render_template, request,jsonify, session, abort
from flask_restful import Resource,Api
from werkzeug.utils import secure_filename
from ocr_tools import ocr_controller as ocr
from config import config as conn  
from file_handlers import file_helper as filehelp
from serverinspectors import logsyncronizer
from flask_cors import CORS
from ocr_tools import base64_handler as bs64
import requests
import os
import time 
from file_handlers import file_writer as file_wr


UPLOAD_FOLDER = conn.ROOT + conn.TEMP_IMAGE
UPLOAD_ZIP = conn.ROOT + conn.TEMP_ZIP

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ZIPPED_FILE'] = UPLOAD_ZIP
api = Api(app)



class OCR_recognize_single(Resource):
    log = logsyncronizer.Logger()
    def post(self):
        if request.method == 'GET' or request.method == 'POST':
            from_add = " Request IP : {x}".format(x=request.remote_addr)
            app.logger.info(from_add)
            temp_json = request.get_json()
            bs64.WrireBase64ToImg(temp_json.get('filename'), temp_json.get('file').encode(), UPLOAD_FOLDER)
            if filehelp.isCheckImgfile_Avail(temp_json.get('filename')):
                string = ocr.Img2Str(temp_json.get('filename'))
                if string[0]:
                    if filehelp.DeleteImageFile(temp_json.get('filename')):
                        if filehelp.Str2Txt(temp_json.get('filename'),string[1]):
                            res = filehelp.isCheckTxtFile_Avail(temp_json.get('filename'))
                            if res[0]:
                                file_wr.filename_writer(str(res[2] + '.txt'))
                                return send_file(res[1],mimetype='text/plain',attachment_filename= res[2] + '.txt',as_attachment=True)
                else:
                    app.logger.warn(from_add + str("Image not convert to text"))
                    return {"Error": "Can not to convert string"}
            else:
                return {"Error": "Server Error"}
        else:
            return {'Error': 'You Cant Access the API'}
                    

class OCR_recognize_Zip(Resource):
    log = logsyncronizer.Logger()
    def post(self):
        if request.method == 'POST':
            from_add = " Request IP : {x}".format(x=request.remote_addr)
            app.logger.info(from_add)
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['ZIPPED_FILE'],filename))
            if filehelp.isCheckImageZip_Avail(filename):
                if filehelp.create_Dir(filename):
                    if filehelp.zip_Extractor(filename):
                        if filehelp.DeleteZipFile(filename):
                            res = filehelp.ReturnListZipFile(filename)
                            if res[0]:
                                if ocr.ZipImg2Str(res[1],res[2]):
                                    res_z = filehelp.Dir_Zipper(res[2],filename)
                                    if res_z[0]:
                                        if filehelp.Remove_dir(res[2]):
                                            file_wr(str(res_z[1]) + '.zip')
                                            return send_file(res_z[1],mimetype='application/zip',attachment_filename= res_z[2] + '.zip',as_attachment=True)
            else:
                return {'Error': 'You Cant Access the API'}



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/urlUploader", methods=['POST'])
def urlUploader():
    if request.method == 'POST':
        return ocr.Url2Str(request.form['url'])


api.add_resource(OCR_recognize_single,'/uploader',methods=['GET','POST'])
api.add_resource(OCR_recognize_Zip,'/zipuploader',methods=['GET','POST'])


if __name__ == '__main__':
    import logging
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format = logFormatStr, filename = "error.log", level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("error.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(fileHandler)
    app.logger.addHandler(streamHandler)
    app.logger.info("Logging is set up.")
    app.run(host='0.0.0.0')
