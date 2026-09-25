# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-25, 09:21 p.m.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    req_list = textwrap.wrap(string,max_width)
    return "\n".join(req_list)
    
