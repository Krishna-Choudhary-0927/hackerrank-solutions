# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-27, 07:15 p.m.
# ──────────────────────────────────────────────────

N,M = [int(x) for x in input().split()]
    
for i in range(1,N,2):
    print((".|."*i).center(M,"-"))
    
print("WELCOME".center(M,"-"))

for i in range(N-2,0,-2):
    print((".|."*i).center(M,"-"))
