def read_write():
    with open('ds.csv', 'r') as fin:
        with open('ds.tsv', 'w') as fout:
            fout.write(fin.read().replace('","', '"\t"')
                                 .replace('false,', 'false\t')
                                 .replace('true,', 'true\t')
                                 .replace('",', '\t'))

if __name__ == '__main__':
    read_write()
    