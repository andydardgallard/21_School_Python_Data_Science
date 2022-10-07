#!/usr/bin/env python3

import os

def main():
    try:
        if os.environ['VIRTUAL_ENV'][-8:] == 'dgallard':
            raise Exception("Wrong VENV")
        os.system('pip3 install Beautifulsoup4 pytest')
        os.system('pip freeze')
        os.system('pip3 freeze > requirements.txt')
    except KeyError:
        print('Wrong enviroment')
    return

if __name__ == '__main__':
    main()