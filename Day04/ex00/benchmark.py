import timeit

class Ex00:
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    domain = "@gmail.com"
    
    def append_method(self): 
        new_list = list()
        for i in self.emails:
            if i.find(self.domain) != -1:
                new_list.append(i)
        return new_list
    
    def comprehens_method(self):
        new_list = [i for i in self.emails if i.find(self.domain) != -1]
        return new_list

if __name__ == '__main__':
    ex00 = Ex00()
    time_append = timeit.timeit(ex00.append_method, number=90000000)
    time_compreh = timeit.timeit(ex00.comprehens_method, number=90000000)
    
    if time_compreh <= time_append:
        print("it is better to use a list comprehension") 
    else:
        print("it is better to use a loop")
        
    print(f'{min(time_append, time_compreh)}' + ' vs ' + 
          f'{max(time_append, time_compreh)}')
    # print(time)