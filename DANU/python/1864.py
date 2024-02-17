def octopus_to_decimal(octopus_num):
    dict_octopus = { '-' : 0,
                     '\\' : 1,
                     '(' : 2,
                     '@' : 3,
                     '?' : 4,
                     '>' : 5,
                     '&' : 6,
                     '%' : 7,
                     '/' : -1 }
    decimal_num = 0
    for digit in octopus_num:
        if digit in dict_octopus:
            decimal_num = (decimal_num * 8) + dict_octopus[digit]

    return decimal_num

def main():
    while True:
        octopus_num = input().strip()
        if octopus_num == '#':  # 입력 종료 조건
            break
        print(octopus_to_decimal(octopus_num))

if __name__ == "__main__":
    main()
