def dedupe_string_cases(n):
    for _ in range(n):
        prev = ''
        s = input()
        result = []
        for i in range(len(s)):
            if prev != s[i]:
                result.append(s[i])
                prev = s[i]
        print("".join(result))

def main():
    n = int(input())
    dedupe_string_cases(n)

if __name__ == "__main__":
    main()
