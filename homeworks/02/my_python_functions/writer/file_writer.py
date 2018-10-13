import os
import pickle as pkl



class FileWriter:
    
    def __init__(self, path):
        if not self._check_path(path):
            os.system("touch " + path)
        self._path = path
        self.file = open(path)
        self.file.close()
    
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
    def path(self, npath):

        if self.file != None:
            self.file.close()
            self.file = None

        if not self._check_path(npath):
            os.system("touch " + npath)
        self._path = npath
        self.file = open(npath)
        self.file.close()

    @path.deleter 
    def path(self):

        if self._path == None:
            return
        
        os.system("rm -rf " + self._path)
        self.file = None
        self._path = None

    def print_file(self):

        if self._path == None and self.file == None:
            raise Exception("print-error")
        if self.file == None:
            if not self._check_path(self._path):
                return
        
        self.file = open(self._path)
        for ln in self.file:
            print(ln)
        self.file.close()
    
    def write(self, some_string):
        if self._path == None:
            raise Exception("write-error")
        if not self._check_path(self._path):
            os.system("touch " + self._path)

        with open(self._path, 'a') as f:
            f.write(some_string)
    
    def save_yourself(self, file_name):
        with open(file_name, 'wb') as f:
            if self.file != None:
                self.file = None
            pkl.dump(self, f)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as f:
            rs = pkl.load(f)
            if rs._path == None:
                raise Exception("load-error")
            if not rs._check_path(rs._path):
                return
            rs.file = open(rs._path)
            rs.file.close()
            return rs
