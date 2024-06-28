def check_players(players):
    if 'anj' in players:
        print('뭐야;')
    else:
        print('뭐야?')

def main():
    n = int(input())
    players = [input() for _ in range(n)]
    check_players(players)

if __name__ == "__main__":
    main()
