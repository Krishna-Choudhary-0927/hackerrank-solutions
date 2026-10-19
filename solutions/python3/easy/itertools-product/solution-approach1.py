# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 10:24 a.m.
# ──────────────────────────────────────────────────

from itertools import product

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
cartesian_product = list(product(A,B))
for i in cartesian_product:
    print(i,end=" ")
