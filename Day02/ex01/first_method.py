class Research:
    def file_reader(self):
        with open('data.csv', 'r') as fin:
            return fin.read()

def main():
    researcher = Research()
    print(researcher.file_reader())

if __name__ == '__main__':
    main()