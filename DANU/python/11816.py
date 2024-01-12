input_value = input()

if len(input_value) == 1 :
    print(input_value)
elif input_value[1] == 'x' :
    print(int(input_value, 16))
elif input_value[0] == '0' :
    print(int(input_value, 8))
else :
    print(input_value)
