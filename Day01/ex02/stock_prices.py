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
    comp_name = sys.argv[1].lower().capitalize()
    if comp_name not in COMPANIES:
        print("Unknown company")
    else:
        print(STOCKS[COMPANIES[comp_name]])
    return

def main():
    if len(sys.argv) == 2:
        handler()
    return

if __name__ == '__main__':
    main()