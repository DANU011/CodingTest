from collections import deque

def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_path():
    queue = deque()
    queue.append(starting_point)

    while queue:
        x, y = queue.popleft()

        if calculate_distance((x, y), destination) <= 1000:
            print('happy')
            return

        for i in range(store_count):
            if i not in visited_stores:
                new_x, new_y = store_locations[i]
                if calculate_distance((x, y), (new_x, new_y)) <= 1000:
                    queue.append([new_x, new_y])
                    visited_stores.add(i)

    print('sad')

test_cases = int(input())

for _ in range(test_cases):
    store_count = int(input())
    starting_point = list(map(int, input().split()))
    store_locations = [list(map(int, input().split())) for _ in range(store_count)]
    destination = list(map(int, input().split()))
    visited_stores = set()
    find_path()