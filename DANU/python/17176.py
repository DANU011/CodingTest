def init_dic():
    word_dit = {" ": 0}
    for i in range(65, 91):
        word_dit[chr(i).upper()] = word_dit.setdefault(chr(i).upper(), i - 64)

    for i in range(97, 123):
        word_dit[chr(i).lower()] = word_dit.setdefault(chr(i).lower(), i - 70)

    return word_dit


def decoding(n, secret_text, plain_text):
    word_dit = init_dic()
    secret_text_sorted = sorted(secret_text)
    arr = sorted([word_dit.get(text) for text in plain_text])
    return 'y' if secret_text_sorted == arr else 'n'


def main():
    n = int(input())
    secret_text = list(map(int, input().split()))
    plain_text = input()

    result = decoding(n, secret_text, plain_text)
    print(result)


if __name__ == "__main__":
    main()
