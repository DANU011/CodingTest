def reorder_and_print(data):
    for i in range(2, len(data)):
        print(data[i], end=' ')
    print(data[0], data[1])

def main():
    n = int(input())
    for _ in range(n):
        data = list(input().split())
        reorder_and_print(data)

if __name__ == "__main__":
    main()
