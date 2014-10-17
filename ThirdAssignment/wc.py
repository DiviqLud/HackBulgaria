import sys


def main():
    counter = 0
    if sys.argv[1] == "chars":
        file = open(sys.argv[2], 'r')
        content = file.read()
        for i in content:
            counter += 1
        file.close()
        print(counter)
    elif sys.argv[1] == "words":
        file = open(sys.argv[2], 'r')
        content = file.read()
        content = content.split()
        for i in content:
            counter += 1
        file.close()
        print(counter)
    elif sys.argv[1] == "lines":
        with open(sys.argv[2], 'r') as myfile:
            lines = len(myfile.readlines())
        print(lines)
    else:
        print("wrong command")
if __name__ == '__main__':
    main()
