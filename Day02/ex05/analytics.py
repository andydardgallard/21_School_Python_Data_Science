from random import randint
import os

class Research:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.calc = self.Calculations(self.file_reader())
        self.analytics = self.Analitycs(self.file_reader())

    def file_reader(self, has_header=True):
        with open(self.file_path, 'r') as fin:
            if not os.access(self.file_path, os.R_OK):
                raise OSError("Can't open file")
            rows = fin.readlines()
        
        if has_header:
            header = rows[0].split(',')
            if len(rows) < 2:
                raise Exception("File has no data")
            if len(header) != 2:
                raise ValueError("Wrong Header")
        else:
            if len(rows) < 1:
                raise Exception("File has no data")

        res = list()
        if has_header:
            for row in rows[1:]:
                row = row.strip()
                if row != '0,1' and row != '1,0':
                    raise Exception("Wrong data")
                res.append([int(n) for n in row.split(',')])
        else:
            for row in rows:
                row = row.strip()
                if row != '0,1' and row != '1,0':
                    raise Exception("Wrong data")
                res.append([int(n) for n in row.split(',')])
        return res
    
    class Calculations:
        def __init__(self, data) -> None:
            self.data = data
        
        def counts(self, data):
            return [sum([el[0] for el in data]), sum([el[1] for el in data])]  
        
        def fractions(self, heads, tails):
            return [heads / (heads + tails) * 100, tails / (heads + tails) * 100]
    
    class Analitycs(Calculations):
        def __init__(self, data) -> None:
            super().__init__(data)
        
        def predict_random(self,  n):
            res = list()
            for i in range(n):
                tmp = randint(0, 1)
                res.append([tmp, (tmp + 1) % 2])
            return res
        
        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, name_of_file, ext='txt'):
            with open(name_of_file + '.' + ext, 'w') as fout:
                fout.write(data)
