def print_game_results(kevin_score, stuart_score):
    if stuart_score > kevin_score:
        print("Stuart " + str(stuart_score))
    elif kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))
    else:
        print("Draw")


def minion_game(text):
    kevin_score = 0
    stuart_score = 0
    vowels = "AEIOU"
    for i in range(len(text)):
        if text[i] in vowels:
            kevin_score += len(text) - i
        else:
            stuart_score += len(text) - i

    print_game_results(kevin_score, stuart_score)


if __name__ == '__main__':
    s = input()
    minion_game(s)
