from file_handlers import file_writer as file_w
from file_handlers import file_helper as file_h
from serverinspectors import logsyncronizer
import time 

def job():
    print("printing")

class FileDeleter:
    def __init__(self):
        self._inspec_periority_min = 100
        self._log = logsyncronizer.Logger()


    def FileAllNames(self):
        file_l = file_w.give_all_filname_list()
        if file_w.del_filenames_file():
            self._log.LogSyncronizer("INFO", "filenames.txt file Deleted Successfully")
            if file_w.create_filenames_file():
                self._log.LogSyncronizer("INFO", "filenames.txt file Created Successfully")
        return file_l

    def _check_file_type(self, filename):
        file_n = filename[-3:]
        if file_n == 'txt':
            return 'txt'
        if file_n == 'zip':
            return 'zip'

    def _delete_txt_file(self, filename):
        if file_h.DeleteTxtFile(filename):
            self._log.LogSyncronizer("INFO", "File {x} is Deleted Successfully".format(x=filename)) 
        else:
            self._log.LogSyncronizer("WARN", "File {x} is Not Deleted".format(x = filename))

        
    def _delete_zip_file(self, filename):
        if file_h.DeleteZipFile(filename):
            self._log.LogSyncronizer("INFO", "File {x} is Deleted Succcessfully".format(x=filename))
        else:
            self._log.LogSyncronizer('WARN', "File {x} is Not Deleted".format(x = filename))

    def FILE_DELETER_GAINT(self):
        print("Success")
        for file_n in self.FileAllNames():
            print(file_n)
            if self._check_file_type(file_n) == 'txt':
                self._delete_txt_file(file_n)
            if self._check_file_type(file_n) == 'zip':
                self._delete_zip_file(file_n)
    
    

if __name__ == "__main__":
    _Inspector_Del = FileDeleter()
    try:
        while True:
            time.sleep(_Inspector_Del._inspec_periority_min)
            _Inspector_Del.FILE_DELETER_GAINT()
    except Exception as e:
        print(e)

   

    
    