def count_emails(a, b):
    a_cnt = a.count('@')
    b_cnt = b.count('@')
    return a_cnt, b_cnt

def main():
    a, b = input().split("(^0^)")
    a_cnt, b_cnt = count_emails(a, b)
    print(a_cnt, b_cnt)

if __name__ == "__main__":
    main()
