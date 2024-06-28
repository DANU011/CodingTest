def check_anagrams(a, b):
    A = sorted(list(a))
    B = sorted(list(b))
    return A == B


def main():
    i = 1

    while True:
        a = input()
        b = input()
        if a == "END" and b == "END":
            break
        else:
            if check_anagrams(a, b):
                print("Case", str(i) + ": same")
            else:
                print("Case", str(i) + ": different")

            i += 1


if __name__ == "__main__":
    main()
