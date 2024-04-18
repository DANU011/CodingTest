def calculate_ascii_sum(name):
    ascii_list = [ord(char) - 64 for char in name]
    return sum(ascii_list)

def main():
    count = int(input())
    name = input()
    result = calculate_ascii_sum(name)
    print(result)

if __name__ == "__main__":
    main()
