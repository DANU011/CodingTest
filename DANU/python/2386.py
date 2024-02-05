while True:
    input_text = input()
    if input_text == '#':
        break
    tokens = input_text.split()
    first_word_upper = tokens[0].upper()
    first_word_lower = tokens[0].lower()
    remaining_text = ' '.join(tokens[1:])
    count_occurrences = remaining_text.count(first_word_upper) + remaining_text.count(first_word_lower)
    print('{0} {1}'.format(first_word_lower, count_occurrences))
