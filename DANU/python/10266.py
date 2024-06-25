def kmptable(a):
    m = len(a)
    table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]
        if a[i] == a[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    table = kmptable(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1
    return False


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    b = list(map(int, data[n + 1:2 * n + 1]))

    clock1 = [0] * 360000
    clock2 = [0] * 360000

    for i in a:
        clock1[i] = 1
    for i in b:
        clock2[i] = 1

    clock1 += clock1

    if kmp(clock1, clock2):
        print("possible")
    else:
        print("impossible")


if __name__ == "__main__":
    main()
