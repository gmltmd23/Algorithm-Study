import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
cards, total = [], 0
for i in range(n):
    card = int(input().rstrip())
    total += card
    heapq.heappush(cards, card)
print(total + heapq.heappop(cards) + heapq.heappop(cards))