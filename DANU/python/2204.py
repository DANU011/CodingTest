def find_first_word():
    while True:
        voca = []
        n = int(input())
        if n == 0:
            return
        for i in range(n):
            voca.append(input())
        voca.sort(key=str.lower)
        print(voca[0])

if __name__ == '__main__':
    find_first_word()
