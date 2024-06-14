from sys import stdin


def classify_pangrams(num_cases, cases):
    results = []

    for i in range(1, num_cases + 1):
        res = 'Not a pangram'
        string = cases[i - 1].rstrip()

        alphabet = [[False] * 26 for _ in range(3)]

        for j in string:
            idx = 0
            if not j.isalpha():
                continue
            else:
                while 1:
                    if not alphabet[idx][ord(j.lower()) - 97]:
                        alphabet[idx][ord(j.lower()) - 97] = True
                        break
                    else:
                        idx += 1

                    if idx > 2:
                        idx = 0
                        break

        cnt = 0
        for data in alphabet:
            if False in data:
                break
            else:
                cnt += 1

        if cnt == 1:
            res = 'Pangram!'
        elif cnt == 2:
            res = 'Double pangram!!'
        elif cnt == 3:
            res = 'Triple pangram!!!'

        results.append('Case {}: {}'.format(i, res))

    return results


def main():
    input = stdin.read
    data = input().splitlines()
    num_cases = int(data[0])
    cases = data[1:num_cases + 1]

    results = classify_pangrams(num_cases, cases)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
