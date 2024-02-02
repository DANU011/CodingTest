result_list = []

while True :
    stack = []
    pair_count = 0
    brackets = input()
    if '-' in brackets :
        break
    for char in brackets :
        if not stack and char == '}' :
            pair_count += 1
            stack.append('{')
        elif stack and char == '}' :
            stack.pop()
        else :
            stack.append(char)
    pair_count += len(stack) // 2
    result_list.append(pair_count)

for idx, result in enumerate(result_list) :
    print(idx + 1, '. ', result, sep='')
