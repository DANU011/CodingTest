import sys

def process_attendance(start, end, stream, data):
    start = int(start[:2] + start[3:])
    end = int(end[:2] + end[3:])
    stream = int(stream[:2] + stream[3:])
    
    attend = set()
    cnt = 0

    for line in data:
        time, name = line.split()
        time = int(time[:2] + time[3:])
        if time <= start:
            attend.add(name)
        elif end <= time <= stream and name in attend:
            attend.remove(name)
            cnt += 1

    return cnt

def main():
    input = sys.stdin.readline
    start, end, stream = input().split()
    data = sys.stdin.readlines()
    result = process_attendance(start, end, stream, data)
    print(result)

if __name__ == "__main__":
    main()
