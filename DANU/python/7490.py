import sys
input = sys.stdin.readline

def dfs(n, idx, rst, ans_sik):
    if idx == n:
        ans = eval(rst.replace(' ', ''))
        if ans == 0:
            ans_sik.append(rst)
        return
    else:
        n_idx = idx + 1
        dfs(n, n_idx, rst + ' ' + str(n_idx), ans_sik)
        dfs(n, n_idx, rst + '+' + str(n_idx), ans_sik)
        dfs(n, n_idx, rst + '-' + str(n_idx), ans_sik)

def find_zero_expressions(N):
    ans_sik = []
    dfs(N, 1, '1', ans_sik)
    return ans_sik

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        results = find_zero_expressions(N)
        for result in results:
            print(result)
        print()

if __name__ == "__main__":
    main()
