# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-18, 06:45 p.m.
# ──────────────────────────────────────────────────

def minion_game(string):
    vowel = {'A','E','I','O','U'}
    kevin = 0
    stuart = 0
    lenth = len(string)
    for i in range(0,lenth):
        if string[i] in vowel:
            kevin += lenth - i
        if string[i] not in vowel:
            stuart += lenth - i
            
    if stuart > kevin:
        print("Stuart",stuart)
    elif stuart < kevin:
        print("Kevin",kevin)
    elif stuart == kevin:
        print("Draw")

