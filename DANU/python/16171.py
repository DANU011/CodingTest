def check_occurrence(s, k):
    word = []
    for i in s:
        if i.isalpha():
            word.append(i)
    word = ''.join(word)
    if k in word:
        return 1
    else:
        return 0

def main():
    s = list(input())
    k = input()
    result = check_occurrence(s, k)
    print(result)

if __name__ == "__main__":
    main()
