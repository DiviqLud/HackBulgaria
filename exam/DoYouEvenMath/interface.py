from expression import Expression
from db_instructions import DBManager
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from base import Base


def main():
    engine = create_engine("sqlite:///doyouevenmath.db")
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    expression = Expression()
    manager = DBManager(session)

    print('''
        Welcome to the "Do you even math?" game!
            Here are your options:
            - start
            - highscores''')

    command = input("Enter> ")
    command = command.split(" ")
    while command[0] != 'end':
        if command[0] == "start":
            username = input("Enter your name: ")
            while True:
                result = expression.generate_math_expr()
                answer = float(input("Your answer is: "))
                if expression.solve_math_expr(result, answer) is False:
                    manager.commit_in_db(username, expression.return_result())
                    break
        if command[0] == "highscores":
            manager.show_highscores()
        command = input("Enter> ")
        command = command.split(" ")


if __name__ == '__main__':
    main()
