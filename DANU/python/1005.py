import sys
from collections import deque

def bfs(queue, in_degrees, time_record):
    while queue:
        building = queue.popleft()
        time = time_record[building]
      
        for neighbor_building in graph[building]:
            in_degrees[neighbor_building] -= 1
          
            if in_degrees[neighbor_building] == 0:
                queue.append(neighbor_building)
            time_record[neighbor_building] = max(time_record[neighbor_building], time + time_list[neighbor_building])

    print(time_record[target_building])

test_cases = int(sys.stdin.readline())

for t in range(test_cases):
    num_buildings, num_relations = list(map(int, sys.stdin.readline().split()))
    time_list = [-1] + list(map(int, sys.stdin.readline().split()))
    graph = {}
    in_degrees = {} 
  
    for i in range(1, num_buildings + 1):
        graph[i] = []
        in_degrees[i] = 0
      
    for i in range(num_relations):
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[x].append(y)
        in_degrees[y] += 1
      
    target_building = int(sys.stdin.readline())

    queue = deque()
    time_record = [-1] + [0 for _ in range(1, num_buildings + 1)]
    for i in range(1, num_buildings + 1):
      
        if in_degrees[i] == 0:
            queue.append(i)
            time_record[i] = time_list[i]
          
    bfs(queue, in_degrees, time_record)
