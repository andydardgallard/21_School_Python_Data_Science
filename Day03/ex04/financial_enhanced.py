import httpx
from bs4 import BeautifulSoup
import sys
import time

def main():
    if len(sys.argv) != 3:
        raise Exception("Wrong Number of ARGs!")
    url = f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials?p={sys.argv[1]}'
    resp = httpx.get(url, headers={'User-Agent': 'Custom'})
    bs = BeautifulSoup(resp.text, 'html.parser')
    title = bs.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticker')
    tags = bs.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if sys.argv[2] not in breakdowns:
        raise Exception('Not found breakdown')
    # time.sleep(5)
    print(tuple(t.get_text() for t in tags[breakdowns.index(sys.argv[2])].find_all('span')))
    
   
    return

if __name__ == "__main__":
    import cProfile
    from pstats import Stats
    from pstats import SortKey

    pr = cProfile.Profile()
    pr.enable()

    main()

    pr.disable()
    stats = Stats(pr)
    stats.sort_stats(SortKey.CUMULATIVE).print_stats(5)
    # try:
    #     main()
    # except Exception as err:
    #     print(type(err).__name__, err, sep=': ')
        
        
# python3 -m cProfile -s time financial_enh.py 'MSFT' 'Total Revenue' > profiling-sleep.txt