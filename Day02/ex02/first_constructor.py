import sys
import os

class Research:
    
    def __init__(self, file_path) -> None:
        self.file_path = file_path
    
    def file_reader(self):
        with open(self.file_path, 'r') as fin:
            if not os.access(self.file_path, os.R_OK):
                raise OSError("Can't open file")
            return fin.readlines()
        
    def handler(self):
        rows = self.file_reader()
        if len(rows) < 2:
            raise Exception("File has no data")
        header = rows[0].split(',')
        if header[0] != 'head' and header[1] != "tail":
            raise Exception("Wrong Header")
        for row in rows[1:]:
            if row[0:3] != '0,1' and row[0:3] != '1,0':
                raise Exception("Wrong data")
        return ''.join(rows)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            reseacher = Research(sys.argv[1])
            print(reseacher.handler())
        else:
            raise Exception("Wrong quantity of args")
    except Exception as err:
        print(err)
    