# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Problem     Alphabet Rangoli
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 01:11 p.m.
# ──────────────────────────────────────────────────

import string
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    
    for i in range(size):
        s = "-".join(alphabet[i:size])
        line = s[::-1] + s[1:]
        lines.append(line.center(4 * size - 3, "-"))
        
    result = lines[::-1] + lines[1:]
    print("\n".join(result))

