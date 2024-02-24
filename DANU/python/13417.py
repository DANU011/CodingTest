from collections import deque

def word_rearrange(num, card):
    word = deque([card[0]])

    for i in card[1:]:
        if i > word[0]:
            word.append(i)
        else:
            word.appendleft(i)
    
    return ''.join(word)

def main():
    num_tests = int(input())
    
    for _ in range(num_tests):
        num = int(input())
        card = list(map(str, input().strip().split()))
        result = word_rearrange(num, card)
        print(result)

if __name__ == "__main__":
    main()
