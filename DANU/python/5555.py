target_word = input()
num_rings = int(input())
matching_count = 0

for _ in range(num_rings) :
    current_ring = input()
    if target_word in current_ring * 2 :
        matching_count += 1
        
print(matching_count)
