# 진호의 mbti 유형 my_mbti = input()
# 진호의 친구의 수 int
# n개의 줄에 친구의 mbti 유형
# 진호와 mbti 유형이 같은 사람의 수 출력
def mbti_check(my_mbti, friends_mbti):
    # count = 0
    # for mbti in friends_mbti:
    #     if mbti == my_mbti:
    #         count += 1
    # return count
    return len([mbti for mbti in friends_mbti if mbti == my_mbti])


if __name__ == "__main__":
    friends_mbti = []
    my_mbti = input()
    for _ in range(int(input())):
        mbti = input()
        friends_mbti.append(mbti)

    print(mbti_check(my_mbti=my_mbti, friends_mbti=friends_mbti))