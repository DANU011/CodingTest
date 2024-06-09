def find_minimum_reversed_string(s):
    li = []
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            for k in range(j + 1, len(s)):
                t = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
                li.append(t)
    return min(li)

def main():
    s = input()
    result = find_minimum_reversed_string(s)
    print(result)

if __name__ == "__main__":
    main()
