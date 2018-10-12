import os
import pickle as pkl
class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_ = path
            self.file = None
        else:
            os.system ("touch " + path)
            self.path=path
            self.file=None
        
    def _check_path(self, path):
        try:
            f=open(path)
            f.close()
            return 1
        except:
            return 0

    def get_path(self):
            return self.path

    def set_path(self,path0):
            self.path=path0

    def delete(self):
        os.system("rm -rf "+self.path)
    
    def print_file(self):
            f=open(self.path)
            for line in f:
                print (line)
            f.close()

    def write(self, some_string):
        with open(self.path,'a') as f_obj:
            f_obj.write(some_string)
            f_obj.write('\n')
    
    def save_yourself(self, file_name):
        with open(file_name, 'wb') as f:
            pkl.dump(self, f)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as f:
            return  pkl.load(f)
stroka='blabla.txt'
try:
    f=FileWriter(stroka)
except:
    os.system("touch " + stroka)
    f=FileWriter(stroka)
