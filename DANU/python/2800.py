from itertools import combinations

def generate_expressions(expr):
    indices = []
    stk = []
    answers = set()

    for i in range(len(expr)):
        if expr[i] == '(':
            stk.append(i)
        elif expr[i] == ')':
            indices.append((stk.pop(), i))

    for i in range(len(indices)):
        for comb in combinations(indices, i+1):
            temp = expr[:]
            for idx in comb:
                temp[idx[0]] = temp[idx[1]] = ""
            answers.add("".join(temp))

    return sorted(list(answers))

def main():
    expr = list(input())
    results = generate_expressions(expr)
    for item in results:
        print(item)

if __name__ == "__main__":
    main()
