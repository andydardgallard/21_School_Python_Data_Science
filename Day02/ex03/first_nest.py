import sys
import os

class Research:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.calc = self.Calculations()

    def file_reader(self, has_header=False):
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
        def counts(self, data):
            return [sum([el[0] for el in data]), sum([el[1] for el in data])]  
        def fractions(self, heads, tails):
            return [heads / (heads + tails) * 100, tails / (heads + tails) * 100]

def main():
    researcher = Research(sys.argv[1])
    try:
        data = researcher.file_reader(has_header=True)
        print(data)
        counts = researcher.calc.counts(data)
        print(counts[0], counts[1])
        fractions = researcher.calc.fractions(counts[0], counts[1])
        print(fractions[0], fractions[1])
    except Exception as err:
        print(type(err).__name__, err, sep=': ')
    
    return

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        raise Exception("Wrong quantity of args")