import sys

def generate_pattern(r, c, a, b):
    type_1 = ''
    type_2 = ''
    for i in range(1, int(c) + 1):
        if i == 1:
            type_1 += "X" * int(b)
            type_2 += "." * int(b)
        elif i != 1 and i % 2 == 0:
            type_1 += "." * int(b)
            type_2 += "X" * int(b)
        else:
            type_1 += "X" * int(b)
            type_2 += "." * int(b)

    result = []
    for j in range(1, int(r) + 1):
        if j == 1:
            for k in range(int(a)):
                result.append(type_1)
        elif j != 1 and j % 2 == 0:
            for k in range(int(a)):
                result.append(type_2)
        else:
            for k in range(int(a)):
                result.append(type_1)
    return result

def main():
    r, c = sys.stdin.readline().rstrip().split()
    a, b = sys.stdin.readline().rstrip().split()

    pattern = generate_pattern(r, c, a, b)
    for line in pattern:
        print(line)

if __name__ == "__main__":
    main()
