def is_palindrome_possible(st):
    front, back = 0, len(st) - 1
    check = 0

    for _ in range(len(st)):
        if front >= back:
            break
        if st[front] == st[back]:
            front += 1
            back -= 1
            continue

        if st[front] == st[back-1]:
            temp = st[front:back]
            if temp[:] == temp[::-1]:
                check = 1
                break
        if st[front+1] == st[back]:
            temp = st[front+1:back+1]
            if temp[:] == temp[::-1]:
                check = 1
                break

        check = 2
        break

    return check

def main():
    num = int(input())
    for _ in range(num):
        st = input().strip()
        print(is_palindrome_possible(st))

if __name__ == "__main__":
    main()
