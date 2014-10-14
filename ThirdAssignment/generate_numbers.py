import sys
from random import randint


def generate_numbers():
    result = ""
    for i in range(0, int(sys.argv[2])):
        a = randint(1, 1000)
        result = result + str(a) + " "
    file = open(sys.argv[1], "w")
    file.write(result)
    file.close()

    file = open(sys.argv[1], "r")
    content = file.read()
    print(content)
    file.close()


def main():
    return generate_numbers()

if __name__ == '__main__':
    main()
