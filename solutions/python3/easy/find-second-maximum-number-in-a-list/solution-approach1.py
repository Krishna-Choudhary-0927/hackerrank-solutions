# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 11:51 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in (input().split())]
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    print(arr[-2])
