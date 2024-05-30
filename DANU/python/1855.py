def transform_string(n, s):
    arr = []
    for i in range(0, len(s), n):
        arr.append(list(s[i:i+n]))

    for i in range(len(arr)):
        if i % 2 != 0:
            arr[i] = list(reversed(arr[i]))

    res = ''
    for j in range(n):
        for i in range(len(arr)):
            res += arr[i][j]
    
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    result = transform_string(n, s)
    print(result)

if __name__ == "__main__":
    main()
