num_test_cases = int(input())

for _ in range(num_test_cases) :
    num_participants = int(input())
    max_score = 0
    max_score_name = ''

    for _ in range(num_participants) :
        current_score, participant_name = input().split()
        current_score = int(current_score)

        if current_score > max_score :
            max_score = current_score
            max_score_name = participant_name

    print(max_score_name)
