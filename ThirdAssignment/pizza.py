import sys


def main():
    listOfChoices = ["take <name> <price>",
                     "status",
                     "save",
                     "list",
                     "load <number>",
                     "finish"]
    print("MAKE YOUR CHOICE")
    print()
    for i in listOfChoices:
        print(i)
    print()
    splitter = listOfChoices[0].split()
    clients = {}
    flag = True
    while flag:
        command = input("Enter command>")
        commandsplitter = command.split()
        if command == listOfChoices[5]:
            break
        elif commandsplitter[0] == splitter[0]:
            if commandsplitter[1] not in clients:
                clients[commandsplitter[1]] = float(commandsplitter[2])
                print(clients)
            else:
                clients[commandsplitter[1]] += float(commandsplitter[2])
                print(clients)
        elif command == listOfChoices[1]:
            for name in clients:
                print(name + " - " + str(clients[name]))
        elif ф

if __name__ == '__main__':
    main()
