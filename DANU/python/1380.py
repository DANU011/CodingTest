def process_data():
    result = []
    n = 1
    while n:
        n = int(input())
        names = [input() for i in range(n)]
        values = []

        for i in range(2 * n - 1):
            a = int(input().split()[0])
            values.append(a)

        values.sort()
        for i in range(0, len(values), 2):
            if i == (len(values) - 1) or values[i] != values[i + 1]:
                result.append(names[values[i] - 1])
                break
    return result

def main():
    result = process_data()
    for i in range(len(result)):
        print(i+1, result[i])

if __name__ == "__main__":
    main()
