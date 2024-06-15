import sys

def count_similar_words(n, words):
    temp = [[] for _ in range(101)]
    dic = [{} for i in range(101)]
    cnt = 0

    for i in range(n):
        num = 0
        m = words[i]

        for j in m:
            if j not in dic[i]:
                dic[i][j] = str(num)
                num += 1

            temp[i] += dic[i][j]

    for i in range(n):
        for j in range(i + 1, n):
            if temp[i] == temp[j]:
                cnt += 1

    return cnt

def main():
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip('\n') for _ in range(n)]
    result = count_similar_words(n, words)
    print(result)

if __name__ == "__main__":
    main()
