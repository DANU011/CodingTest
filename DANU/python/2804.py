word_A, word_B = input().split()
rows, cols = len(word_A), len(word_B)
puzzle = [['.'] * rows for _ in range(cols)]

for i, char_A in enumerate(word_A) :
    if char_A in word_B :
        row = word_B.index(char_A)
        col = i
        break

for i, char_A in enumerate(word_A) :
    puzzle[row][i] = char_A

for i, char_B in enumerate(word_B) :
    puzzle[i][col] = char_B

for row in puzzle :
    print(''.join(row))
