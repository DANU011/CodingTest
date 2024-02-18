def parse_input():
    n = int(input())
    matches = []
    for _ in range(n):
        win, time = input().split()
        matches.append((win, time))
    return n, matches

def calculate_time(minutes, seconds):
    return minutes * 60 + seconds

def calculate_match_time(matches):
    prev = [0, 0]
    team1 = [0, 0]
    team2 = [0, 0]
    for win, time in matches:
        if win == '1':
            team1[0] += 1
        else:
            team2[0] += 1
        minutes, seconds = map(int, time.split(":"))
        time_in_seconds = calculate_time(minutes, seconds)
        if team1[0] == team2[0]:
            if prev[1] == 1:
                team1[1] += time_in_seconds - prev[0]
            else:
                team2[1] += time_in_seconds - prev[0]
            prev[1] = 0
        elif team1[0] > team2[0]:
            if prev[1] == 0:
                prev[0] = time_in_seconds
                prev[1] = 1
        else:
            if prev[1] == 0:
                prev[0] = time_in_seconds
                prev[1] = 2

    if prev[1] == 1:
        team1[1] += 48 * 60 - prev[0]
    if prev[1] == 2:
        team2[1] += 48 * 60 - prev[0]

    return team1[1], team2[1]

def format_time(minutes, seconds):
    return "%02d:%02d" % (minutes // 60, minutes % 60)

def main():
    n, matches = parse_input()
    team1_time, team2_time = calculate_match_time(matches)
    print(format_time(team1_time, 0))
    print(format_time(team2_time, 0))

if __name__ == "__main__":
    main()
