def sum_digitwise(a, b):
    la, lb = len(a), len(b)
    if la > lb:
        b = '0' * (la - lb) + b
    else:
        a = '0' * (lb - la) + a
    res = ""
    for i in range(len(a)):
        res += str(int(a[i]) + int(b[i]))
    return res

def main():
    a, b = input().split()
    result = sum_digitwise(a, b)
    print(result)

if __name__ == "__main__":
    main()
