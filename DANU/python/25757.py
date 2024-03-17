def calculate_nicknames(n, game, nicknames):
    games = {"Y": 1, "F": 2, "O": 3}
    return len(set(nicknames)) // games[game]

def main():
    n, game = input().split()
    nicknames = []
    for _ in range(int(n)):
        nicknames.append(input())
        
    result = calculate_nicknames(n, game, nicknames)
    print(result)

if __name__ == "__main__":
    main()
