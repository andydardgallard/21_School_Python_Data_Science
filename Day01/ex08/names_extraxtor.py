import sys

def main():
    if len(sys.argv) != 2:
        raise Exception("Wrong Number of Args!")
    try:
        with open(sys.argv[1], 'r') as fin:
            with open("employees.tsv", 'w') as fout:
                fout.write("Name\tSurname\tE-mail\n")
                mails = fin.read().split('\n')
                for i in mails:
                    name = i.split('.')
                    surname = i.split('@')[0].split('.')
                    fout.write(f'{name[0].capitalize()}\t{surname[1].capitalize()}\t{i}\n')
    except Exception as err:
        print(type(err).__name__, err, sep=': ')
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(type(err).__name__, err, sep=': ')