def count_occurrences_of_k(n, k):
    k = str(k)
    count = 0

    time_strings = (
        f"{hour:02}{minute:02}{second:02}"
        for hour in range(n + 1)
        for minute in range(60)
        for second in range(60)
    )
    count = sum(1 for time_string in time_strings if k in time_string)

    return count

def main():
    n, k = map(int, input().split())
    result = count_occurrences_of_k(n, k)
    print(result)

if __name__ == "__main__":
    main()
