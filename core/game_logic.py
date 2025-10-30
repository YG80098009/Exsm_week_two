

def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    for i in hand:
        if i["rank"] in ["J","Q","K","A"]:
            if i["rank"] == "A":
                total += 1
            else:
                total += 10
        else:
            total += int(i["rank"])
    return total


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        player["hand"].append(deck.pop())
        dealer["hand"].append(deck.pop())
    return

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    sam = deck
    while sam <= 17:
        sam = calculate_hand_value(deck)
        if sam > 17 and sam <= 21:
            return True
        else:
            print("lose")
            return False

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    return None


# player = {
#     "hand": [] # list of cards (dicts)
# }
# dealer = {
#     "hand": [] # list of cards (dicts)
# }