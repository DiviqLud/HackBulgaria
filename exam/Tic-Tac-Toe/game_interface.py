from ai import AI


def main():
    game = AI()

    print ('''Let's play TicTacToe
                  Type start!''')

    command = input("Type> ")
    command = command.split(' ')
    if command[0] == "start":
        game.flip_coin()
        game.print_board()
        choice = input("Enter your choice: ")
        while True:
            if game.player_move(choice) is True:
                print("Player wins")
                break
            if game.full_board():
                print('The game is a tie!')
                break
            if game.computer_move() is True:
                print("Computer wins")
                break
            choice = input("Enter your choice: ")

if __name__ == '__main__':
    main()
