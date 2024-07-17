def sol(origin, changed):
    for i in range(len(origin)):
        if origin[i] != changed[i]:
            return 'ERROR'
    return 'OK'

def process_inputs(t, input_list):
    results = []
    for i in range(t):
        origin, changed = input_list[i].split()
        results.append(sol(origin, changed))
    return results

def main():
    t = int(input())
    input_list = [input() for _ in range(t)]
    results = process_inputs(t, input_list)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
