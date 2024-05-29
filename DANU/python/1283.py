def process_sentence(sentence, exist):
    words = list(sentence.split())
    flag = False 

    for i in range(len(words)):
        if words[i][0].upper() not in exist:
            exist.append(words[i][0].upper())
            flag = True 
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            return ' '.join(words)
    
    if not flag:
        for i in range(len(words)):
            check = False 
            for j in range(len(words[i])):
                if words[i][j].upper() not in exist:
                    exist.append(words[i][j].upper())
                    flag = True 
                    check = True 
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
                    return ' '.join(words)
            if check: 
                break 
    
    return ' '.join(words)

def main():
    n = int(input())
    exist = []
    for _ in range(n):
        sentence = input()
        result = process_sentence(sentence, exist)
        print(result)

if __name__ == "__main__":
    main()
