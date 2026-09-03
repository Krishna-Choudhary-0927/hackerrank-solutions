# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-03, 10:10 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
this question has old hashing answer and python has changed hashing
so right answer also will give wrong value, also my answer was:
n = int(input())
t = tuple([int(x) for x in input().split()])
print(hash(t))
'''
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    # Reproduce the pre-Python-3.8 64-bit tuple hash algorithm
    mask = (1 << 64) - 1

    x = 0x345678
    mult = 1000003
    length = len(t)

    for item in t:
        y = hash(item)

        x = ((x ^ y) * mult) & mask

        length -= 1
        mult += 82520 + length + length
        mult &= mask

    x = (x + 97531) & mask

    # Convert unsigned 64-bit result to signed 64-bit integer
    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    print(x)
