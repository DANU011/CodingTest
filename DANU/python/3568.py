def process_string(string):
    string_list = string.split(' ')
    basic_type = string_list[0]
    del string_list[0]

    result = []
    
    for s in string_list:
        s = s.replace(",", '').replace(";", '')
        processed_string = basic_type

        for i in range(len(s) - 1, 0, -1):
            if not s[i].isalpha():
                if s[i] == ']':
                    processed_string += '['
                elif s[i] == '[':
                    processed_string += ']'
                else:
                    processed_string += s[i]

        processed_string += ' '

        for i in range(len(s)):
            if s[i].isalpha():
                processed_string += s[i]

        processed_string += ';'
        
        result.append(processed_string)
    
    return result

def main():
    string = input()
    processed_strings = process_string(string)
    for processed_string in processed_strings:
        print(processed_string)

if __name__ == "__main__":
    main()
