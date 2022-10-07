from random import randint
import os
import logging
import requests
from config import *

class Research:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler('analytics.log', mode='w')
        self.logger.addHandler(self.handler)
        self.formatter = logging.Formatter(fmt='%(asctime)s %(message)s')
        self.handler.setFormatter(self.formatter)
        self.__file_reader = 0
        self.data = self.file_reader()
        self.calc = self.Calculations(self.data, self.logger)
        self.analytics = self.Analitycs(self.data, self.logger)

    def file_reader(self, has_header=True):
        if self.__file_reader != 0:
            self.logger.debug('Read '+ self.file_path)
        self.__file_reader += 1
        with open(self.file_path, 'r') as fin:
            if not os.access(self.file_path, os.R_OK):
                raise OSError("Can't open file")
            rows = fin.readlines()
        
        if has_header:
            header = rows[0].split(',')
            if len(rows) < 2:
                self.logger.error("File has no data")
                self.send_report(fail, webhook, token, chat_id)
            if len(header) != 2:
                self.logger.error("Wrong Header")
                self.send_report(fail, webhook, token, chat_id)
        else:
            if len(rows) < 1:
                self.logger.error("File has no data")
                self.send_report(fail, webhook, token, chat_id)

        res = list()
        if has_header:
            for row in rows[1:]:
                row = row.strip()
                if row != '0,1' and row != '1,0':
                    self.logger.error("Wrong data")
                    self.send_report(fail, webhook, token, chat_id)
                res.append([int(n) for n in row.split(',')])
        else:
            for row in rows:
                row = row.strip()
                if row != '0,1' and row != '1,0':
                    self.logger.error("Wrong data")
                    self.send_report(fail, webhook, token, chat_id)
                res.append([int(n) for n in row.split(',')])
        return res

    def send_report(self, message, webhook, token, chat_id):
       
        url_req = webhook + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message 
        results = requests.get(url_req)
        if results.status_code != 200:
            raise Exception(f'Error server {results.status_code}')
    
    class Calculations:
        def __init__(self, data, logger) -> None:
            self.data = data
            self.logger = logger
        
        def counts(self, data):
            self.logger.debug('Calculating the counts of heads and tails')
            return [sum([el[0] for el in data]), sum([el[1] for el in data])]  
        
        def fractions(self, heads, tails):
            self.logger.debug('Calculating the counts of heads and tails')
            return [heads / (heads + tails) * 100, tails / (heads + tails) * 100]
    
    class Analitycs(Calculations):
        def __init__(self, data, logger) -> None:
            super().__init__(data, logger)
        
        def predict_random(self,  n):
            self.logger.debug('Predict the random of heads and tails')
            res = list()
            for i in range(n):
                tmp = randint(0, 1)
                res.append([tmp, (tmp + 1) % 2])
            return res
        
        def predict_last(self):
            self.logger.debug('Predict the random of heads and tails')
            return self.data[-1]

        def save_file(self, data, name_of_file, ext='txt'):
            self.logger.debug('Save data to ' + name_of_file+ '.' + ext)
            with open(name_of_file + '.' + ext, 'w') as fout:
                fout.write(data)