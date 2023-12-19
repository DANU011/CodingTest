import sys
input = sys.stdin.readline

n, m = input().split()
n_lst = list(map(int, n))
m_lst = list(map(int, m))

print(sum(n_lst) * sum(m_lst))
