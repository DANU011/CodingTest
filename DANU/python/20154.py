def calculate_winner(s, alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ', numbers='32123333113133122212112221'):
    cnt = 0
    for i in range(len(s)):
        cnt += int(numbers[alpha.index(s[i])])
        cnt %= 10
    return "You're the winner?" if cnt % 2 == 0 else "I'm a winner!"

def main():
    s = input()
    result = calculate_winner(s)
    print(result)

if __name__ == "__main__":
    main()
