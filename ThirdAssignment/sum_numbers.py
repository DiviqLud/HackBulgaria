import sys


def main():
    file = open(sys.argv[1], "r")
    content = file.read()
    content = content.split()
    sum = 0
    for number in content:
        sum += int(number)
    print(sum)
    file.close()

if __name__ == '__main__':
    main()
