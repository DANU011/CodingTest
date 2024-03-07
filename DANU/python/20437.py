import sys

def find_substrings(t, words):
    results = []

    for w, k in words:
        count_char_dict = {}
        for char in w:
            count_char_dict[char] = count_char_dict.get(char, 0) + 1

        check = False
        max_answer = -1
        min_answer = len(w)
        check_dict = {}

        for i in range(len(w)):
            if count_char_dict[w[i]] < k:
                continue

            check = True
            check_dict[w[i]] = check_dict.get(w[i], []) + [i]

        for key, value_list in check_dict.items():
            for i in range(len(value_list) - k + 1):
                max_answer = max(max_answer, value_list[i+k-1] - value_list[i] +1)
                min_answer = min(min_answer, value_list[i + k - 1] - value_list[i] + 1)

        if check:
            results.append((min_answer, max_answer))
        else:
            results.append(-1)
    return results

def main():
    input_function = sys.stdin.readline

    t = int(input_function())
    words = []

    for _ in range(t):
        w = input_function().rstrip()
        k = int(input_function())
        words.append((w, k))

    results = find_substrings(t, words)

    for result in results:
        if isinstance(result, tuple):
            print(result[0], result[1])
        else:
            print(result)

if __name__ == "__main__":
    main()
