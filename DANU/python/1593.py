import sys


def count_valid_substrings(g, s, W, S):
    answer = 0
    alphabets = {}
    for x in W:
        alphabets[x] = alphabets.get(x, 0) + 1

    current_count = {}
    for i in range(g):
        current_count[S[i]] = current_count.get(S[i], 0) + 1

    if current_count == alphabets:
        answer += 1

    for i in range(1, s - g + 1):
        current_count[S[i - 1]] -= 1
        if current_count[S[i - 1]] == 0:
            del current_count[S[i - 1]]

        current_count[S[i + g - 1]] = current_count.get(S[i + g - 1], 0) + 1

        if current_count == alphabets:
            answer += 1

    return answer


def main():
    g, s = map(int, input().split())
    W = sys.stdin.readline().strip()
    S = sys.stdin.readline().strip()
    result = count_valid_substrings(g, s, W, S)
    print(result)


if __name__ == "__main__":
    main()
