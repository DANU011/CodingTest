def find_ith_handle(N, I, handles):
    handles.sort()
    return handles[I-1]

def main():
    N, I = map(int, input().split())
    handles = [input() for _ in range(N)]
    result = find_ith_handle(N, I, handles)
    print(result)

if __name__ == "__main__":
    main()
