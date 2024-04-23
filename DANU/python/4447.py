from collections import Counter

def evaluate_string(s):
    cnt = 0
    for char, count in Counter(s).items():
        if char.lower() == 'g':
            cnt += count
        elif char.lower() == 'b':
            cnt -= count
    
    if cnt > 0:
        return f"{s} is GOOD"
    elif cnt == 0:
        return f"{s} is NEUTRAL"
    else:
        return f"{s} is A BADDY"

def main():
    N = int(input())
    for _ in range(N):
        S = input()
        result = evaluate_string(S)
        print(result)

if __name__ == "__main__":
    main()
