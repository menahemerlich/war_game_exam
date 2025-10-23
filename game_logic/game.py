from war_game_esam.utils.deck import shuffle, create_deck


def create_player(*name:str) -> dict:
    player = {}
    if len(name) == 0:
        player["name"] = "AI"
    else:
        player["name"] = name[0]
    player["hand"] = []
    player["won_pile"] = []
    return player

def init_game()->dict:
    game_dict = {}
    p1 = create_player("erlich")
    p2 = create_player()
    new_deck = shuffle(create_deck())
    p1["hand"] = new_deck[:26]
    p2["hand"] = new_deck[26:]
    game_dict["deck"] = new_deck
    game_dict["player_1"] = p1
    game_dict["player_2"] = p2
    return game_dict

def play_round(p1:dict,p2:dict):
    pass

