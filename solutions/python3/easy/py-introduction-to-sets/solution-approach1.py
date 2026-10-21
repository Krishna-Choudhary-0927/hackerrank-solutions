# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-21, 09:35 a.m.
# ──────────────────────────────────────────────────

def average(array):
    set_array = set(array)
    sum = 0
    for i in set_array:
        sum += i
    avg = sum/len(set_array)
    return round(avg,3)
    
