import timeit
import random
from collections import Counter

class Ex04:
    rnd_list = [random.randint(0, 100) for i in range(10000)]
    
    def __init__(self) -> None:
        pass
    
    def my_function(self):
        dctr = dict.fromkeys(set(self.rnd_list), 0)
        for i in self.rnd_list:
            if i in dctr:
                dctr[i] += 1
        return dctr
 
    def my_top_funct(self):
        dctr = dict.fromkeys(set(self.rnd_list), 0)
        for i in self.rnd_list:
            if i in dctr:
                dctr[i] += 1
        sorted_dct = sorted(dctr.items(), key=lambda item: item[1], reverse=True)
        return sorted_dct[:10]

    def func_cntr(self):
        return(dict(Counter(self.rnd_list)))

    def func_top_cnter(self):
        return dict(Counter(self.rnd_list).most_common(10))
    
    def handler(self):
        print(f'my function: {timeit.timeit(self.my_function, number=1000)}')
        print(f'Counter: {timeit.timeit(self.func_cntr, number=1000)}')
        print(f'my top: {timeit.timeit(self.my_top_funct, number=1000)}')
        print(f'Counter\'s top: {timeit.timeit(self.func_top_cnter, number=1000)}')

if __name__ == "__main__":
    try:
            ex04 = Ex04()
            ex04.handler()
    except Exception as err:
        print(err)
    