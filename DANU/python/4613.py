def calculate_string_value(s, alphabet=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    result = 0
    for i in range(len(s)):
        result += alphabet.index(s[i]) * (i + 1)
    return result

def main():
    while True:
        string = input().strip()
        if string == '#':
            break
        print(calculate_string_value(string))

if __name__ == "__main__":
    main()
