from collections import defaultdict

def file_clean(n) :
    file_count = defaultdict(int)

    for _ in range(n) :
        file_extension = input().split('.')[1]
        file_count[file_extension] += 1

    for extension, count in sorted(file_count.items()) :
        print(extension, count)

n = int(input())
file_clean(n)
