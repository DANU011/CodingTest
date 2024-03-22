def count_non_prefix_words(words):
    sorted_words = sorted(words, key=len)
    res = 0

    for i in range(len(sorted_words)):
        if not any(sorted_words[i] == sorted_words[j][:len(sorted_words[i])] for j in range(i + 1, len(sorted_words))):
            res += 1

    return res

def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    print(count_non_prefix_words(words))

if __name__ == "__main__":
    main()
