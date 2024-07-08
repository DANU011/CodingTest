def count_keywords(s):
    cnt = 0
    cnt += s.count("for")
    cnt += s.count("while")
    return cnt

def find_max_value(c, inputs):
    max_value = 0
    for s in inputs:
        cnt = count_keywords(s)
        max_value = max(max_value, cnt)
    return max_value

def main():
    c = int(input())
    inputs = [input() for _ in range(c)]
    max_value = find_max_value(c, inputs)
    print(max_value)

if __name__ == "__main__":
    main()
