import heapq
import sys

n = int(input())
card_deck = []

for _ in range(n):
    heapq.heappush(card_deck, int(sys.stdin.readline()))

if len(card_deck) == 1:
    print(0)
else:
    ans = 0
    while len(card_deck) > 1:
        temp_1 = heapq.heappop(card_deck)
        temp_2 = heapq.heappop(card_deck)
        ans += temp_1 + temp_2
        heapq.heappush(card_deck, temp_1 + temp_2)
    
    print(ans)
