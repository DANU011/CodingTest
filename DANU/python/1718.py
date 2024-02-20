def alpha_to_num(c):
    return ord(c) - ord('a')

def num_to_alpha(n):
    return chr((n % 26) + ord('a'))

sent = input().rstrip()
sec_key = input().rstrip()

ans = ''
for i in range(len(sent)):
    if sent[i] == ' ':
        ans += ' '
        continue
    now = alpha_to_num(sent[i]) - alpha_to_num(sec_key[i % len(sec_key)]) - 1
    if now < 0:
        now += 26
    ans += num_to_alpha(now)

print(ans)
