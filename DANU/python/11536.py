def line_up(names):
    if names == sorted(names):
        return "INCREASING"
    elif names == sorted(names, reverse=True):
        return "DECREASING"
    else:
        return "NEITHER"

def main():
    num_names = int(input())
    names = [input() for _ in range(num_names)]
    result = line_up(names)
    print(result)

if __name__ == "__main__":
    main()
