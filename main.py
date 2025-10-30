from core.deck import build_standard_deck
from core.game_logic import calculate_hand_value,deal_two_each,dealer_play,run_full_game
from core.player_io import ask_player_action

if __name__ == "__main__":
    pass

player = {"hand": []}
dealer = {"hand": []}

#print(run_full_game(create_deck(), player, dealer))

#print(build_standard_deck())

#print(calculate_hand_value(build_standard_deck()))

#print(deal_two_each(build_standard_deck(),{"hand": [] },{"hand": []}))
sam = calculate_hand_value(build_standard_deck())
print(dealer_play(sam,{"hand": []}))

#print(ask_player_action())