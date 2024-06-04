import sys
si = sys.stdin.readline
test_cases = int(si())

def dfs(char_count_dict, current_anagram, characters):
    if len(current_anagram) == len(characters):
        print("".join(current_anagram))
        return
    
    for char in char_count_dict:
        if char_count_dict[char]:
            char_count_dict[char] -= 1
            current_anagram.append(char)
            dfs(char_count_dict, current_anagram, characters)
            char_count_dict[char] += 1
            current_anagram.pop()
    return

for _ in range(test_cases):
    characters = list(map(str, si().rstrip()))
    characters.sort()
    char_count_dict = {}
    for char in characters:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    
    dfs(char_count_dict, [], characters)
