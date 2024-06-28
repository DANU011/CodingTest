def count_unique_alphabets():
    while True:
        s = input()
        if s == '#':
            break
        lst = [0] * 26
        for i in s.lower():
            if i.isalpha():
                lst[ord(i) - 97] = 1
        print(lst.count(1))

def main():
    count_unique_alphabets()

if __name__ == "__main__":
    main()
