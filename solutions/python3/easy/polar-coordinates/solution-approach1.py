# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 11:26 a.m.
# ──────────────────────────────────────────────────

import cmath
z = complex(input())
x = z.real
y = z.imag
print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))
