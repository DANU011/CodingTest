def count_and_replace(s, word):
    cnt = s.count(word)
    replaced_s = s.replace(word, "")
    return cnt + len(replaced_s)

def main():
    n = int(input())
    for _ in range(n):
        s, word = map(str, input().split())
        result = count_and_replace(s, word)
        print(result)

if __name__ == "__main__":
    main()
