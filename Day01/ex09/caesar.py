import sys

def main():
    if len(sys.argv) != 4:
        raise Exception("incorrect number of arguments is given")
    text = sys.argv[2]
    try:
        text.encode('ascii')
    except UnicodeEncodeError:
        raise Exception("The script does not support your language yet")
    shift = int(sys.argv[3])
    if sys.argv[1] == 'decode':
        shift *= -1
    elif sys.argv[1] != 'encode':
        raise Exception("Wrong command")
    lower = list('abcdefghijklmnopqrstuvwxyz')
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    res =''
    for char in text:
        if char in lower:
            res += lower[(lower.index(char) + shift) % 26]
        elif char in upper:
            res += upper[(upper.index(char) + shift) % 26]
        else:
            res += char
    print(res)
    return

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(type(err).__name__, err, sep=': ')