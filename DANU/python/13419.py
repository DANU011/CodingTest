def process_game(game):
    if len(game) % 2 == 0:
        print(game[0::2])
        print(game[1::2])
    else:
        print(game[0::2], game[1::2], sep='')
        print(game[1::2], game[0::2], sep='')


def main():
    t = int(input())
    games = [input() for _ in range(t)]

    for game in games:
        process_game(game)


if __name__ == "__main__":
    main()
