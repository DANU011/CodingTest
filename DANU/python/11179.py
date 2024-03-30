def decimal_to_reversed_binary(n):
    binary_str = bin(n)[2:]
    reversed_binary_str = binary_str[::-1]
    return int(reversed_binary_str, 2)

def main():
    n = int(input())
    reversed_binary_decimal = decimal_to_reversed_binary(n)
    print(reversed_binary_decimal)

if __name__ == "__main__":
    main()
