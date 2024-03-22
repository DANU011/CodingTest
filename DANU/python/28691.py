def get_club_name(first_letter):
    if first_letter == 'M':
        return 'MatKor'
    elif first_letter == 'W':
        return 'WiCys'
    elif first_letter == 'C':
        return 'CyKor'
    elif first_letter == 'A':
        return 'AlKor'
    elif first_letter == '$':
        return '$clear'

def main():
    first_letter = input().strip()
    club_name = get_club_name(first_letter)
    print(club_name)

if __name__ == "__main__":
    main()
