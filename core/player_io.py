

def ask_player_action() -> str:
    get_val = input("enter S/H")
    while get_val not in ["S","H"]:
        get_val = input("enter S/H")
    return get_val



