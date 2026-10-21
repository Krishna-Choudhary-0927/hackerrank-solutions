# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-21, 10:19 a.m.
# ──────────────────────────────────────────────────

from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    d[word].append(str(i))
    
for _ in range(m):
    word = input().strip()
    if word in d:
        print(" ".join(d[word]))
    else:
        print(-1)
