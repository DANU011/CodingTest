import sys

input_stream = sys.stdin.readline

hour1, minute1, second1 = map(int, input_stream().split(':'))
hour2, minute2, second2 = map(int, input_stream().split(':'))

time1_seconds = hour1 * 60 * 60 + minute1 * 60 + second1
time2_seconds = hour2 * 60 * 60 + minute2 * 60 + second2

time_difference = (
    time2_seconds - time1_seconds
    if time2_seconds > time1_seconds
    else time2_seconds - time1_seconds + 24 * 60 * 60
)

hours = time_difference // 60 // 60
minutes = (time_difference // 60) % 60
seconds = time_difference % 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))
