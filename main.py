from war_game_esam.game_logic.game import init_game, play_round

if __name__ == "__main__":
    new_game = init_game()
    while len(new_game["player_1"]["hand"]) > 0 or len(new_game["player_2"]["hand"]) > 0:
        play_round(new_game["player_1"],new_game["player_2"])
        play_round(new_game["player_1"], new_game["player_2"])

    if len(new_game["player_1"]["won_pile"]) > len(new_game["player_2"]["won_pile"]):
        print(f'{new_game["player_1"]["name"]} (player_1) is teh winner')
    elif len(new_game["player_1"]["won_pile"]) < len(new_game["player_2"]["won_pile"]):
        print(f'{new_game["player_2"]["name"]} (player_2) is teh winner')
    else:
        print("WAR!!")




