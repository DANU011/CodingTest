def expand_pattern(R, C, ZR, ZC):
    expanded_lines = []
    for _ in range(R):
        line = input()
        expanded_line = "".join([char * ZC for char in line])
        for _ in range(ZR):
            expanded_lines.append(expanded_line)
    return expanded_lines

def main():
    R, C, ZR, ZC = map(int, input().split())
    for line in expand_pattern(R, C, ZR, ZC):
        print(line)

if __name__ == "__main__":
    main()
