import os
import pickle as pkl


class FileWriter:
    
    def __init__(self, path):
        if not self._check_path(path):
            os.system("touch " + path) 
        self._path = path
        self.file = True
    
    def _check_path(self, path):
        try:
            f = open(path)
            f.close()
            return 1
        except:
            return 0
    
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, pathe):

        if self.file != False:
            self.file = False

        if not self._check_path(pathe):
            os.system("touch " + pathe)
        self._path = pathe
        self.file = True

    @path.deleter 
    def path(self):
        self.file = False
        self._path = None

    def print_file(self):

        
        if self._path == None and self.file == False:
            raise Exception("print-no file")
        if self.file == False:
            if not self._check_path(self._path):
                return
        
        f = open(self._path)
        for ln in f:
            print(ln)
        f.close()

    def write(self, some_string):
        if self._path == None:
            raise Exception("write-no file")
        if not self._check_path(self._path):
            self.file = True
            os.system("touch " + self._path)

        with open(self._path, 'a') as f:
            f.write(some_string)
    
    def save_yourself(self, file_name):
        with open(file_name, 'wb') as f:
            if self.file != False:
                self.file = False
            pkl.dump(self, f)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as f:
            rs = pkl.load(f)
            if rs._path == None:
                raise Exception("load-no file")
            if not rs._check_path(rs._path):
                rs.file = False
                return rs
            rs.file = True
            return rs

