import os

def filename_writer(filename):
    if filenames_file_is_Avail('./file_names/filenames.txt'):
        with open('./file_names/filenames.txt', 'a') as writer:
            writer.writelines(filename + '\n')
            writer.close()
    else:
        if create_filenames_file():
            filename_writer(filename)
    return True

def give_all_filname_list():
    return open('./file_names/filenames.txt').readlines()

def filenames_file_is_Avail(path):
    if os.path.exists(path):
        return True
    return False

def create_filenames_file():
    with open('./file_names/filenames.txt', 'w') as writer:
        writer.close()
    return True 

def del_filenames_file(path='./file_names/filenames.txt'):
    os.remove(path)
    if filenames_file_is_Avail(path):
        return False 
    return True

