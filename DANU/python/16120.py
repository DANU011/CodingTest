import sys

def check_ppap(s):
    ppap = []
    ans = 'NP'
    
    for i in s:
        ppap.append(i)
        if len(ppap) >= 4 and ppap[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(3):
                ppap.pop()
    
    if len(ppap) == 1 and ppap[0] == 'P':
        ans = 'PPAP'
    
    return ans

def main():
    input_func = sys.stdin.readline
    s = input_func().rstrip()
    result = check_ppap(s)
    print(result)

if __name__ == "__main__":
    main()
