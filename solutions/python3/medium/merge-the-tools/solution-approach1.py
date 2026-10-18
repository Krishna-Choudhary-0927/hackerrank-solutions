# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-18, 08:59 p.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    string_list = [string[i:i+k] for i in range(0, len(string), k)]
    for i in string_list:
        string_list[string_list.index(i)] = "".join(dict.fromkeys(i))
    for i in string_list:
        print(i)

