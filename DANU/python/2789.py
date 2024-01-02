restricted_chars = list('CAMBRIDGE')
output_string = ''
for char in input() :
    if char not in restricted_chars :
        output_string += char
print(output_string, sep='')
