import sys

words = []
for _ in range(5):  
  s = sys.stdin.readline().rstrip()
  words.append(s)

for i in range(15): 
  for j in range(5): 
    if i < len(words[j]):
      print(words[j][i], end='')
