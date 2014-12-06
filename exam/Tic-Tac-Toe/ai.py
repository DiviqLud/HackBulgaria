from random import random, choice


class AI():
    def __init__(self):
        self.board = ['.'] * 10
        self.free_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        print("  " + self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print("  " + self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print("  " + self.board[1] + '|' + self.board[2] + '|' + self.board[3])

    def flip_coin(self):
        choice = random()
        if choice <= 0.5:
            self.player_sign = 'x'
            self.ai_sign = 'o'
            print("You are with " + self.player_sign)
        else:
            self.player_sign = 'o'
            self.ai_sign = 'x'
            print("You are with " + self.player_sign)

    def is_winning(self, sign, board):
        return ((board[1] == sign and board[2] == sign and board[3] == sign) or
                (board[4] == sign and board[5] == sign and board[6] == sign) or
                (board[7] == sign and board[8] == sign and board[9] == sign) or
                (board[1] == sign and board[4] == sign and board[7] == sign) or
                (board[2] == sign and board[5] == sign and board[8] == sign) or
                (board[3] == sign and board[6] == sign and board[9] == sign) or
                (board[1] == sign and board[5] == sign and board[9] == sign) or
                (board[3] == sign and board[5] == sign and board[7] == sign))

    def move_free(self, choice, board):
        return board[int(choice)] == '.'

    def able_to_move(self, choice):
        while self.move_free(choice, self.board) is False:
            choice = input("Enter your choice: ")

    def choose_random_move(self, free_moves):
        possible_moves = []
        for i in free_moves:
            if self.move_free(i, self.board):
                possible_moves.append(i)
        if len(possible_moves) != 0:
            return choice(possible_moves)
        else:
            return None

    def player_move(self, choice):
        if self.move_free(choice, self.board) is True:
            self.board[int(choice)] = self.player_sign
            self.free_moves.remove(int(choice))
            self.print_board()
        if self.is_winning(self.player_sign, self.board):
            return True

    def make_move(self, letter, move, board):
        board[move] = letter

    def copy_board(self, board):
        duplicate_board = []

        for i in self.board:
            duplicate_board.append(i)

        return duplicate_board

    def ai_try_to_win(self):
        for move in self.free_moves:
            copy = self.copy_board(self.board)
            if self.move_free(move, copy) is True:
                self.make_move(self.ai_sign, move, copy)
                if self.is_winning(self.ai_sign, copy):
                    return move

    def ai_try_to_block(self):
        for move in self.free_moves:
            copy = self.copy_board(self.board)
            if self.move_free(move, copy) is True:
                self.make_move(self.player_sign, move, copy)
                if self.is_winning(self.player_sign, copy):
                    return move

    def ai_smart_move(self):
        print("Computer's turn")

        if self.ai_try_to_win() is not None:
            return self.ai_try_to_win()

        if self.ai_try_to_block() is not None:
            return self.ai_try_to_block()

        if self.move_free('5', self.board) is True:
            return 5

        move = self.choose_random_move([1, 3, 7, 9])
        if move is not None:
            return move

        return self.choose_random_move([2, 4, 6, 8])

    def computer_move(self):
        if self.full_board() is True:
            return False
        self.make_move(self.ai_sign, self.ai_smart_move(), self.board)
        self.print_board()
        if self.is_winning(self.ai_sign, self.board):
            return True

    def full_board(self):
        for spot in range(1, 10):
            if self.move_free(spot, self.board):
                return False
        return True

    #for i in range(1, 10):
    #    if isSpaceFree(board, i):
    #        return False
    #return True











        #for i in range(1, 10):
        #    copy = copy_board(self.board)
        #    if move_free(copy, i):
        #        makeMove(copy, computerLetter, i)
        #        if isWinner(copy, computerLetter):
        #            return i
        # Check if the player could win on his next move, and block them.
        #for i in range(1, 10):
        #    copy = getBoardCopy(board)
        #    if isSpaceFree(copy, i):
        #        makeMove(copy, playerLetter, i)
        #        if isWinner(copy, playerLetter):
        #            return i
        #elif self.board[]
