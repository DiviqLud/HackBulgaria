import random


class Expression():
    def __init__(self):
        self.list_of_op = ['+', '-', '*', '/', '^']
        self.result = 0

    def generate_math_expr(self):
        self.operand1 = random.randint(0, 10)
        self.operand2 = random.randint(0, 10)
        self.operation = random.choice(self.list_of_op)
        op1 = str(self.operand1)
        op2 = str(self.operand2)
        print("What is the answer to " + op1 + self.operation + op2)
        if self.operation == '+':
            return self.operand1 + self.operand2
        elif self.operation == '-':
            return self.operand1 - self.operand2
        elif self.operation == '*':
            return self.operand1 * self.operand2
        elif self.operation == '/':
            if self.operand2 == 0:
                return 0
            else:
                return round((self.operand1 / self.operand2), 2)
        else:
            return self.operand1 ** self.operand2

    def solve_math_expr(self, result, answer):
        if answer == result:
            print("Correct answer")
            self.result += 1
            return True
        else:
            print("You are wrong the answer is " + str(result))
            print(self.return_result())
            return False

    def return_result(self):
        return self.result*self.result


def main():
    a = Expression()
    print(a.generate_math_expr())

if __name__ == '__main__':
    main()
