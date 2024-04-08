def check_mobis(word):
    MOBIS = ['M', 'O', 'B', 'I', 'S']
    for i in MOBIS:
        if i not in word:
            return False
    return True

if __name__ == "__main__":
    word = input()
    if check_mobis(word):
        print('YES')
    else:
        print('NO')
