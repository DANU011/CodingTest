from collections import Counter

def check_letters():
    while True:
        S = Counter(input())
        if S['*'] == 1:
            break
        if S[' '] >= 1:
            del S[' ']
        if len(S) >= 26:
            print('Y')
        else:
            print('N')

if __name__ == "__main__":
    check_letters()
