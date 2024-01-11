number_mapping = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                  '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

start_range, end_range = map(int, input().split())
result_list = []

for num in range(start_range, end_range + 1) :
    translated_str = ' '.join([number_mapping[digit] for digit in str(num)])
    result_list.append([num, translated_str])

result_list.sort(key=lambda x: x[1])

for index, item in enumerate(result_list) :
    if index % 10 == 0 and index != 0 :
        print()
    print(item[0], end=' ')
