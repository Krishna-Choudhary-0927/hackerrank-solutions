# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 11:10 a.m.
# ──────────────────────────────────────────────────

from itertools import permutations
S,k = input().split()
permutation_arr = list(permutations(S,int(k)))
permutation_arr.sort()
for i in permutation_arr:
    print("".join(i))
