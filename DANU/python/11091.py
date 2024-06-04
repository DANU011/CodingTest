def check_pangram(sentence):
    sentence = sentence.lower()
    missing_alphabet = ''
    for alphabet_ascii in range(ord('a'), ord('z') + 1):
        if sentence.find(chr(alphabet_ascii)) == -1:
            missing_alphabet += chr(alphabet_ascii)
    if missing_alphabet == '':
        return "pangram"
    else:
        return f"missing {missing_alphabet}"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    results = []
    for i in range(1, N + 1):
        sentence = data[i]
        result = check_pangram(sentence)
        results.append(result)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
