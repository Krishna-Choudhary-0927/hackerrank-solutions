# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Problem     Exceptions
# Difficulty  Easy
# Subdomain   Errors and Exceptions
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-25, 11:51 a.m.
# ──────────────────────────────────────────────────

T = int(input())
for i in range(T):
    a,b = [x for x in input().split()]
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")
