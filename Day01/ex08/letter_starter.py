import sys

def main():
    if len(sys.argv) != 2:
        raise Exception("Wrong Number of Args!")
    mail = sys.argv[1]
    try:
        with open("employees.tsv", 'r') as fin:
            line = fin.readlines()
            for i in line[1:]:
                name = i.split('\t')[0].strip()
                mylo = i.split('\t')[2].strip()
                if mylo == mail:
                    print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with)' +
                            'you. That’s a precondition for the professionals that our company hires.')
                else:
                    raise Exception("No such e-mail")
    except Exception as err:
        print(type(err).__name__, err, sep=': ')
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(type(err).__name__, err, sep=': ')