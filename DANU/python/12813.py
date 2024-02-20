def calculate_operations(arr):
    max_val = max(arr)
    cnt = 0
    while max_val > 0:
        if max_val % 2 == 0:
            max_val //= 2
        else:
            cnt += 1
            max_val -= 1
        max_val = max(max_val, max(arr))
    return cnt

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = calculate_operations(arr)
    print(result)

if __name__ == "__main__":
    main()
