
# Model for each player
class Player:

    def __init__(self, team, nick, name, nationality, age, kdratio, headshots, majors_won, majors_played) -> None:
        self.team = team
        self.nick = nick
        self.name = name
        self.nationality = nationality
        self.age = age
        self.kdratio = kdratio
        self.headshots = headshots
        self.majors_won = majors_won
        self.majors_played = majors_played

    def __str__(self) -> str:
        return f'Team {self.team}, Nick {self.nick}, Name {self.name}, Nationality {self.nationality}, Age {self.age}, K/D Ratio {self.kdratio}, Headshots {self.headshots}, Majors won {self.majors_won}, Majors played {self.majors_played}'