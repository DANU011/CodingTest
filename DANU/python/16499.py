def count_unique_sorted_words(n, words):
    arr = []
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        if sorted_word not in arr:
            arr.append(sorted_word)
    return len(arr)

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    result = count_unique_sorted_words(n, words)
    print(result)

if __name__ == "__main__":
    main()
