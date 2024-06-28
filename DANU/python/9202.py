import sys

input = sys.stdin.readline

dy = [1, 1, 1, 0, -1, -1, -1, 0]
dx = [1, -1, 0, 1, 1, -1, 0, -1]
score = [0, 0, 0, 1, 1, 2, 3, 5, 11]


def update(word, dictionary):
    now = dictionary
    for w in word:
        if not now.get(w):
            now[w] = {}
        now = now[w]
    now[0] = 1


def find(y, x, bit, now, word, board, words):
    if now.get(0):
        words.add(word)
    for i in range(8):
        y1, x1 = y + dy[i], x + dx[i]
        if 4 > y1 >= 0 and 4 > x1 >= 0:
            if bit & (1 << y1 * 4 + x1):
                continue
            w = board[y1][x1]
            if now.get(w):
                find(y1, x1, bit | (1 << y1 * 4 + x1), now[w], word + w, board, words)


def main():
    dictionary = {}
    num_words = int(input())
    for _ in range(num_words):
        update(input().strip(), dictionary)

    input()  # Read empty line

    num_boards = int(input())
    results = []
    for _ in range(num_boards):
        board = [input().strip() for i in range(4)]
        words = set()
        for y in range(4):
            for x in range(4):
                if dictionary.get(board[y][x]):
                    find(y, x, 1 << y * 4 + x, dictionary[board[y][x]], board[y][x], board, words)
        total_score = sum([score[len(i)] for i in words])
        longest_word = sorted([(-len(i), i) for i in words])[0][1]
        num_words_found = len(words)
        results.append((total_score, longest_word, num_words_found))
        input()  # Read empty line

    for result in results:
        print(result[0], result[1], result[2])


if __name__ == "__main__":
    main()