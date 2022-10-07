#!/usr/bin/env python3
import os

def main():
    # for i in os.environ: 
    #     print(i, '------' + os.environ[i])
    print("Your current virtual env is " + os.environ['VIRTUAL_ENV'])
    return

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
        
        
# dgallard@at-f4 Desktop % cd test 
# dgallard@at-f4 test % python3 -m venv test
# dgallard@at-f4 test % source test/bin/activate