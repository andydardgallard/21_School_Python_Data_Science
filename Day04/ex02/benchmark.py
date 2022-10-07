import timeit
import sys

class Ex02:
    cmds = list(["loop", "list_comprehension", "map", "filter"])
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    domain = "@gmail.com"
    
    def __init__(self, arg, nmbr) -> None:
        self.arg = arg
        self.nmbr = nmbr
    
    def append_method(self): 
        new_list = list()
        for i in self.emails:
            if i.find(self.domain) != -1:
                new_list.append(i)
        return new_list
    
    def comprehens_method(self):
        new_list = [i for i in self.emails if i.find(self.domain) != -1]
        return new_list
    
    def map_method(self):
        def apply_func(c: str):
            if c.find(self.domain) != -1:
                return c
        return list(map(apply_func, self.emails))
    
    def filter_method(self):
        def apply_func(c: str):
            if c.find(self.domain) != -1:
                return c
        return list(filter(apply_func, self.emails))
    
    def handler(self):
        if self.arg == self.cmds[0]:
            print(timeit.timeit(self.append_method, number=int(self.nmbr)))
        elif self.arg == self.cmds[1]:
            print(timeit.timeit(self.comprehens_method, number=int(self.nmbr)))
        elif self.arg == self.cmds[2]:
            print(timeit.timeit(self.map_method, number=int(self.nmbr)))
        elif self.arg == self.cmds[3]:
            print(timeit.timeit(self.filter_method, number=int(self.nmbr)))
        else:
            raise Exception("Wrong command!")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            ex02 = Ex02(sys.argv[1], sys.argv[2])
            ex02.handler()
        else:
            raise Exception("Wrong quantity of args!")
    except Exception as err:
        print(err)
    