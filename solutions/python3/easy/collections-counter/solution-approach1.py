# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 10:46 a.m.
# ──────────────────────────────────────────────────

num_shoes = int(input())
shoes_list = [int(x) for x in input().split()]
num_customers = int(input())
income = 0
for _ in range(num_customers):
    a,b = [int(x) for x in input().split()]
    if a in shoes_list:
        income += b
        shoes_list.remove(a)
print(income)
