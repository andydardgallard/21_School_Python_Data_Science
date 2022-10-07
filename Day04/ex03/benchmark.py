import timeit
import sys
from functools import reduce

class Ex03:
    cmds = list(["loop", "reduce"])
    
    def __init__(self, arg, nmbr, intgr) -> None:
        self.arg = arg
        self.nmbr = nmbr
        self.intgr = intgr
    
    def loop_method(self): 
        sum = 0
        for i in range(int(self.intgr)):
            sum = sum + ((i + 1) * (i + 1))
        return sum
    
    def reduce_method(self):
        def sum(prev, next):
            return prev + next**2
        return(reduce(sum, range(1, int(self.intgr) + 1)))
    
    def handler(self):
        if self.arg == self.cmds[0]:
            print(timeit.timeit(self.loop_method, number=int(self.nmbr)))
        elif self.arg == self.cmds[1]:
            print(timeit.timeit(self.reduce_method, number=int(self.nmbr)))
        else:
            raise Exception("Wrong command!")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            ex03 = Ex03(sys.argv[1], sys.argv[2], sys.argv[3])
            ex03.handler()
        else:
            raise Exception("Wrong quantity of args!")
    except Exception as err:
        print(err)
    