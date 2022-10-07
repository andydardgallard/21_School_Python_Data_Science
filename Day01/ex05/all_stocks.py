import sys

def handler():
    COMPANIES = {
            'Apple': 'AAPL',
            'Microsoft': 'MSFT',
            'Netflix': 'NFLX',
            'Tesla': 'TSLA',
            'Nokia': 'NOK'
    }
    STOCKS = {
            'AAPL': 287.73,
            'MSFT': 173.79,
            'NFLX': 416.90,
            'TSLA': 724.88,
            'NOK': 3.37
    }
    cmnd_name = sys.argv[1].replace(' ', '').split(',')
    for i in cmnd_name:
        if not i:
            print('\n')
            return
    for i in cmnd_name:
        if i.lower().capitalize() in COMPANIES:
            i = i.lower().capitalize()
            print(i + " stock price is", STOCKS[COMPANIES[i]])
        elif i.upper() in STOCKS:
            i = i.upper()
            for j in COMPANIES:
                if COMPANIES[j] == i:
                    print(i + " is a ticker symbol for", j)
        else:
            print(i + " is an unknown company or an unknown ticker symbol")
    return

def main():
    if len(sys.argv) == 2:
        handler()
    return
if __name__ == '__main__':
    main()