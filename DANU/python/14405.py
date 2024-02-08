input_string = input()
substrings = ["pi", "ka", "chu"]

for sub in substrings:
    input_string = input_string.replace(sub, " ")

if input_string.strip() == "":
    print("YES")
else:
    print("NO")
