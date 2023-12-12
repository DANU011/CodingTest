input_dish = list(str(input()))
total_points = 0

for i in range(len(input_dish)) :
    if i == 0 :
        total_points += 10
    elif input_dish[i] == input_dish[i - 1] :
        total_points += 5
    else :
        total_points += 10

print(total_points)
