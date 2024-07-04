def count_mismatches(stst, N):
    cnt = 0
    for i in range(N // 2):
        if stst[i] != stst[-1 - i]:
            cnt += 1
    return cnt

def main():
    N = int(input())
    stst = list(input())
    result = count_mismatches(stst, N)
    print(result)

if __name__ == "__main__":
    main()
