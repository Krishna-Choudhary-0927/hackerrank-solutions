# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 12:01 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest_score = sorted(list(set(score for name, score in records)))[1]
    result = sorted([name for name, score in records if score == second_lowest_score])
    for name in result:
        print(name)
