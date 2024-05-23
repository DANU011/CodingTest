def process_dna(n, s):
    dna = {"AA": "A", "AG": "C", "AC": "A", "AT": "G", "GA": "C", "GG": "G",
           "GC": "T", "GT": "A", "CA": "A", "CG": "T", "CC": "C", "CT": "G",
           "TA": "G", "TG": "A", "TC": "G", "TT": "T"}

    while True:
        if len(s) == 1:
            break
        ss = s[-2] + s[-1]
        if ss in dna:
            del s[-2:]
            s.append(dna.get(ss)) 
    print(*s)

def main():
    n = int(input())
    s = list(input())
    process_dna(n, s)

if __name__ == "__main__":
    main()
