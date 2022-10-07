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

    cmp_tckr = sys.argv[1].upper()
    if cmp_tckr not in STOCKS:
        print("Unknown ticker")
    else:
        for item in COMPANIES:
           if COMPANIES[item] == cmp_tckr:
               print(item, STOCKS[cmp_tckr])
    return

def main():
    if len(sys.argv) == 2:
        handler()
    return

if __name__ == '__main__':
    main()