def palindrome(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len):
            if i != j:
                word = arr[i] + arr[j]
                if word == word[::-1]:
                    return word
    return 0

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [input() for _ in range(n)]
        ans = palindrome(arr)
        print(0) if ans == 0 else print(ans)
        t -= 1

if __name__ == "__main__":
    main()
