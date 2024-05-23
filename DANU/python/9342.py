import re

def check_infection(test):
    pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')
    if pattern.match(test) is None:
        return 'Good'
    else:
        return 'Infected!'

def main():
    t = int(input())
    results = []
    for _ in range(t):
        test = input()
        result = check_infection(test)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
