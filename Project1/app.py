import Crawler
from pymongo import MongoClient
from Player import Player

def main():
    player_list = Crawler.get_records()

    # Database connection
    myclient = MongoClient("mongodb://localhost/player_list")
    #myclient = MongoClient("mongodb+srv://admin:admin@cluster0.xos6s.mongodb.net/baza?retryWrites=true&w=majority")
    db = myclient["player_list"]
    collection = db["player_list"]

    # Converting players in list to json
    player_json = []
    id = 0
    for player in player_list:
        id = id+1
        player_json.append({
            "_id": id,
            "team": player.team,
            "nickname": player.nick,
            "name": player.name,
            "nationality": player.nationality,
            "age": player.age,
            "kdratio": player.kdratio,
            "headshots": player.headshots,
            "majors_won": player.majors_won,
            "majors_played": player.majors_played,
        })
    # Inserting json players to database
    collection.insert_many(player_json)


if __name__ == "__main__":
    main()