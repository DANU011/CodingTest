import sys

def find_words(r, c, graph):
    word = []

    for i in range(r):
        width_word = ""
        for j in range(c):
            if graph[i][j] != "#":
                width_word += graph[i][j]
            elif len(width_word) >= 2:
                word.append(width_word)
                width_word = ""
            else:
                width_word = ""
        if len(width_word) >= 2:
            word.append(width_word)

    for i in range(c):
        length_word = ""
        for j in range(r):
            if graph[j][i] != "#":
                length_word += graph[j][i]
            elif len(length_word) >= 2:
                word.append(length_word)
                length_word = ""
            else:
                length_word = ""
        if len(length_word) >= 2:
            word.append(length_word)

    word.sort()
    return word[0] if word else ""

def main():
    r, c = map(int, sys.stdin.readline().split())
    graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
    result = find_words(r, c, graph)
    print(result)

if __name__ == "__main__":
    main()
