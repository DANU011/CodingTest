def count_gifticons(n):
    gifticon = 0
    for _ in range(n):
        period = input()
        if int(period[2:]) <= 90:
            gifticon += 1
    return gifticon

def main():
    n = int(input())
    gifticon_count = count_gifticons(n)
    print(gifticon_count)

if __name__ == "__main__":
    main()
