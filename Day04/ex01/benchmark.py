import timeit

class Ex01:
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
    
    def map_method(self):
        def apply_func(c: str):
            if c.find(self.domain) != -1:
                return c
        return list(map(apply_func, self.emails))

if __name__ == '__main__':
    ex01 = Ex01()
    results = {"time_append":0, "time_compreh":0, "time_map":0}
    results["time_append"] = timeit.timeit(ex01.append_method, number=9000)
    results["time_compreh"] = timeit.timeit(ex01.comprehens_method, number=9000)
    results["time_map"] = timeit.timeit(ex01.map_method, number=9000)
    
    dict_sortted = sorted(results.items(), key=lambda item: item[1])
    
    if dict_sortted[0][0] == "time_append":
        print("it is better to use a loop")
    elif dict_sortted[0][0] == "time_compreh":
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a map")

    print(f'{dict_sortted[0][1]}' + ' vs ' + 
          f'{dict_sortted[1][1]}' + ' vs ' +
          f'{dict_sortted[2][1]}')
    
    
    print(ex01.map_method())