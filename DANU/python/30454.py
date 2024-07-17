def count_zebra_stripes(n, m, z):
    result = 0
    max_result = 0

    for i in range(n):
        one_count = 0
        if z[i][0] == 1:
            one_count += 1

        for j in range(1, m):
            if z[i][j-1] == 0 and z[i][j] == 1:
                one_count += 1

        if max_result < one_count:
            max_result = one_count
            result = 1
        elif max_result == one_count:
            result += 1

    return max_result, result

def main():
    n, m = map(int, input().split())
    z = [list(map(int, input().strip())) for _ in range(n)]
    max_result, result = count_zebra_stripes(n, m, z)
    print(max_result, result)

if __name__ == "__main__":
    main()
