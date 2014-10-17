import sys


def main():
    for i in range(1, len(sys.argv)):
        file = open(sys.argv[i], 'r')
        content = file.read()
        with open("MEGATRON.txt", 'a+') as myfile:
            myfile.write(content)
            myfile.close()
        file.close()
    file = open("MEGATRON.txt", "r")
    content = file.read()
    print(content)
    file.close()

if __name__ == '__main__':
    main()
