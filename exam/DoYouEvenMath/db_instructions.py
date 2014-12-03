from player import Player


class DBManager():
    def __init__(self, session):
        self.__session = session

    def player_already_in_db(self, username):
        players = self.__session.query(Player).all()
        for player in players:
            if player.username == username:
                return True

    def player_score_in_db(self, username):
        players = self.__session.query(Player).all()
        for player in players:
            if player.username == username:
                return player.score

    def commit_in_db(self, username, score):
        if self.player_already_in_db(username) is True:
            if self.player_score_in_db(username) < score:
                self.__session.query(Player).filter(
                    Player.username == username).update(
                    {"score": score})
                self.__session.commit()
        else:
            player = Player(username=username, score=score)
            self.__session.add(player)
            self.__session.commit()

    def show_highscores(self):
        top_players = self.__session.query(Player).filter(
            Player.id < 10).order_by(Player.score).all()
        for player in reversed(top_players):
            print("{} - {}".format(player.username, player.score))
