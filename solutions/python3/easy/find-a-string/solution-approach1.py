# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-22, 04:32 p.m.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    i = string.find(sub_string)
    count = 0
    while i != -1:
        count += 1
        string = string[i+1:]
        i = string.find(sub_string)
    return count

