def is_reverse_same(input_str):
    reversed_str = input_str[::-1]
    return reversed_str == input_str

def main():
    n = input()
    result = is_reverse_same(n)
    if result:
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    main()
