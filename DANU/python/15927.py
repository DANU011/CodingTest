import sys, math

def palindrome_check(S):
    l = len(S)
    if S == S[0] * l:
        return -1
    elif S[:l//2][::-1] == S[math.ceil(l/2):]:
        return l - 1
    else:  
        return l

def main():
    input = sys.stdin.readline
    S = input().strip()
    result = palindrome_check(S)
    print(result)

if __name__ == "__main__":
    main()
