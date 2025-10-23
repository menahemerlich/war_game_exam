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
    pass

def play_round(p1:dict,p2:dict):
    pass

