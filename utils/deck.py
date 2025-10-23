

def create_card(rank:str,suite:str) -> dict:
    card = {}
    list_nume = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    card["rank"] = rank
    card["suite"] = suite
    if rank == "A":
        card["value"] = 14
    elif rank == "K":
        card["value"] = 13
    elif rank == "Q":
        card["value"] = 12
    elif rank == "J":
        card["value"] = 11
    elif rank in list_nume:
        card["value"] = int(rank)
    else:
        print("Typo error!")
    return card

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    else:
        return "WAR"

def create_deck() -> list[dict]:
    deck = []
    card = {}
    Keys = ["rank", "suite", "value"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suite = ["H", "C", "D", "S"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(len(rank)):
        for j in suite:
            card["rank"] = rank[i]
            card["suite"] = j
            card["value"] = value[i]
            deck.append(card)
            card = {}
    return deck

def shuffle(deck:list[dict]) -> list[dict]:
