import random


def build_standard_deck() -> list[dict]:
    suite = ["H", "C", "D", "S"]
    rank = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}
    ls = []
    for i in suite:
        for v in rank:
            ls.append({
                "rank": v,
                "suite":i,
            })
    return ls
build_standard_deck()


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    random.shuffle(deck)
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        flag = True
        while flag:
            i = random.randint(0,5)
            index_1 = deck[i]
            j = random.randint(0,5)
            index_2 = deck[j]
            temp_d = {"H": 5, "C": 3, "D": 2, "S": 7}
            if i != j:
                for k in temp_d:
                    if index_1["suite"] == k and i % temp_d[k] == 0:
                        print("good")
                        index_1,index_2 = index_2,index_1
                        break
                    else:
                        continue

