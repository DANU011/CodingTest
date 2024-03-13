def decode_string(num_groups, encoded_string):
    group_list = []
    for i in range(0, num_groups * 6, 6):
        group_list.append(encoded_string[i: i + 6])
    promises = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']

    decoded_string = ''
    incorrect_count = 0
    for group in group_list:
        incorrect_count = 0
        for promise in promises:
            correct_count = 0
            for index in range(6):
                if group[index] == promise[index]:
                    correct_count += 1
            if correct_count >= 5:
                decoded_string += chr(promises.index(promise) + 65)
                break
            else:
                incorrect_count += 1
        if incorrect_count == len(promises):
            return str(group_list.index(group) + 1)
    return decoded_string

def main():
    num_groups = int(input())
    encoded_string = input()
    decoded_result = decode_string(num_groups, encoded_string)
    if len(decoded_result) == num_groups:
        print(decoded_result)
    else:
        print(decoded_result)
        quit()

if __name__ == "__main__":
    main()
