# 진호의 mbti 유형 my_mbti = input()
# 진호의 친구의 수 int
# n개의 줄에 친구의 mbti 유형
# 진호와 mbti 유형이 같은 사람의 수 출력
def count_same_mbti(my_mbti, friends_mbti) :
    # count = 0
    # for mbti in friends_mbti:
    #     if mbti == my_mbti:
    #         count += 1
    # return count
    return len([mbti for mbti in friends_mbti if mbti == my_mbti])

def get_friends_mbti() :
    friends_mbti = []
    num_friends = int(input())
    for _ in range(num_friends) :
        mbti = input()
        friends_mbti.append(mbti)
    return friends_mbti

def main() :
    my_mbti = input()
    friends_mbti = get_friends_mbti()
    print(count_same_mbti(my_mbti=my_mbti, friends_mbti=friends_mbti))

if __name__ == "__main__":
    main()