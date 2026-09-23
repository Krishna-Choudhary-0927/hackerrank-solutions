# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Problem     String Validators
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-23, 10:14 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    s = input()
    print(any(item.isalnum() for item in s))
    print(any(item.isalpha() for item in s))
    print(any(item.isdigit() for item in s))
    print(any(item.islower() for item in s))
    print(any(item.isupper() for item in s))
