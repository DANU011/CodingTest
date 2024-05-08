def check_cards(n):
    cards = {
        'STRAWBERRY': 0,
        'BANANA': 0,
        'LIME': 0,
        'PLUM': 0
    }
    
    for _ in range(n):
        fruit, count = input().split()
        cards[fruit] += int(count)
    
    return 5 in cards.values()

def main():
    N = int(input())
    if check_cards(N):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
