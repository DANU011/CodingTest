num_elements, iterations = map(int, input().split())
numbers = list(map(int, input().split(',')))

for _ in range(iterations):
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    numbers = differences

print(*numbers, sep=',')
