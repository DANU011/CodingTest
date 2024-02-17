def process_text(sentence):
    vowels = "aeiou"
    processed_sentence = ""
    i = 0
    while i < len(sentence):
        processed_sentence += sentence[i]
        if sentence[i] in vowels:
            i += 3
        else:
            i += 1
    return processed_sentence

def main():
    input_sentence = input().strip()
    processed_sentence = process_text(input_sentence)
    print(processed_sentence)

if __name__ == "__main__":
    main()
