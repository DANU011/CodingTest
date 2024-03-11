def calculate_hidden_number(n, word):
    d = '0123456789'
    hidden_num = ''
    for w in word:
        if w in d:
            hidden_num += w
        else:
            hidden_num += ' '
    return sum(map(int, hidden_num.split()))

def main():
    n = int(input())
    word = list(input())
    result = calculate_hidden_number(n, word)
    print(result)

if __name__ == "__main__":
    main()
