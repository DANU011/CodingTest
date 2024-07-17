def process_word(word):
    if word == '#':
        return None

    tex = list(word)
    fix = ['a', 'e', 'i', 'o', 'u']
    s = 0

    for i in tex:
        if i in fix:
            s = 1
            break

    if s == 0:
        tex.extend('ay')
        return ''.join(tex)

    for i in range(len(tex)):
        if tex[0] in fix:
            break
        else:
            y = tex.pop(0)
            tex.append(y)

    tex.extend('ay')
    return ''.join(tex)


def main():
    while True:
        word = input()
        result = process_word(word)
        if result is None:
            break
        print(result)



if __name__ == "__main__":
    main()
