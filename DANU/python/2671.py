import re

def check_signal(signal):
    pattern = re.compile('(100+1+|01)+')
    ans = pattern.fullmatch(signal)
    if ans:
        return "SUBMARINE"
    else:
        return "NOISE"

def main():
    signal = input()
    result = check_signal(signal)
    print(result)

if __name__ == "__main__":
    main()
