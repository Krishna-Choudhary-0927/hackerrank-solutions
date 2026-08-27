# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-27, 11:18 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    req_str = ""
    for i in range(1,n+1):
        req_str += str(i)
    print(req_str)
