num_rows = int(input())
pattern = [input() for _ in range(num_rows)]
flip_type = int(input())

if flip_type == 1 :
    print(*pattern, sep='\n')
elif flip_type == 2 :
    print(*[row[::-1] for row in pattern], sep='\n')
else :
    print(*pattern[::-1], sep='\n')
