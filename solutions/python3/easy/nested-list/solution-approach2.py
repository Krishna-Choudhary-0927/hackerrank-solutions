# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-01, 09:19 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    info = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        info.append([name,score])
    sec_min_score = sorted(list(set([score for name,score in info])))[1]
    req_student_names = sorted([name for name,score in info if score == sec_min_score])
    for name in req_student_names:
        print(name)
