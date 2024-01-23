from collections import deque

mistakes_count = 0
n = int(input())
questions_queue = deque()

for i in range(n * 2) :
    if i < n :
        question = input()
        questions_queue.append(question)
    else :
        answer = input()
        if answer != questions_queue[0] :
            questions_queue.remove(answer)
            mistakes_count += 1
        else :
            questions_queue.popleft()

print(mistakes_count)
