def check_first_letters(N, li):
    s = set()
    for i in range(N):
        s.add(li[i][0])
    return 1 if len(s) == 1 else 0

def main():
    N = int(input())
    li = input().split()
    result = check_first_letters(N, li)
    print(result)

if __name__ == "__main__":
    main()
