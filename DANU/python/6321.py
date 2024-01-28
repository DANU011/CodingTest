num_strings = int(input())

for string_num in range(1, num_strings + 1):
    input_data = input()
    transformed_result = ''
    
    for char in input_data:
        char_value = ord(char) + 1
        if char_value > 90:
            char_value = 65
        transformed_result += chr(char_value)
    
    print('String #%d' % string_num)
    print(transformed_result)
    print()
