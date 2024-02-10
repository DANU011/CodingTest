num_count = int(input(''))
num_list = []
for i in range(num_count):
    num_input = input('')
    num_list.append(num_input)
counter = 1

while(1):
    if len({i[-counter:] for i in num_list}) == num_count:
        print(counter)
        break
    counter = counter + 1
