from war_game_esam.utils.deck import shuffle, create_deck, compare_cards


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

def play_round(player_1: dict, player_2: dict):

    p1_card = player_1["hand"].pop(0)
    p2_card = player_2["hand"].pop(0)
    victory = compare_cards(p1_card, p2_card)
    #print(victory)
    if victory == "p1":
        player_1["won_pile"].append(p1_card)
        player_1["won_pile"].append(p2_card)
        #print("Player_1 is the winner.")
    if victory == "p2":
        player_2["won_pile"].append(p1_card)
        player_2["won_pile"].append(p2_card)
        #print("Player_2 is the winner.")
    #if victory == "WAR":
        #print("WAR")


