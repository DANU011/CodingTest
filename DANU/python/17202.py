def process_inputs(a, b):
    arr = [0] * 16
    for i in range(16):
        if i % 2 == 0:
            arr[i] = int(a[i // 2])
        else:
            arr[i] = int(b[i // 2])

    while len(arr) != 2:
        temp = []
        for i in range(len(arr) - 1):
            num = (arr[i] + arr[i + 1]) % 10
            temp.append(num)
        arr = temp

    return ''.join(map(str, arr))

def main():
    a = input().strip()
    b = input().strip()
    result = process_inputs(a, b)
    print(result)

if __name__ == "__main__":
    main()
