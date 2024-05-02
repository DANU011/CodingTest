def process_input(data):
    if data == 'P=NP':
        return 'skipped'
    else:
        a, b = map(int, data.split('+'))
        return a + b

def main():
    n = int(input())
    for _ in range(n):
        data = input()
        result = process_input(data)
        print(result)

if __name__ == "__main__":
    main()
