def calculate_difference(a):
    word = 'ILOVEYONSEI'
    result = 0

    for i in range(len(word)):
        result += abs(ord(word[i]) - ord(a))
        a = word[i]

    return result

def main():
    a = input()
    result = calculate_difference(a)
    print(result)

if __name__ == "__main__":
    main()
