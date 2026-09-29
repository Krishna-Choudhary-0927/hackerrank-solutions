# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 06:00 p.m.
# ──────────────────────────────────────────────────

# def print_formatted(number):
    # len_num = len(str(f"{number:b}"))
    # for i in range(1,number+1):
    #     a = str(i)
    #     b = str(oct(i)[2:])
    #     c = str(f"{i:x}")
    #     d = str(f"{i:b}")
    #     print(a.rjust(len_num," "),b.rjust(len_num," "),c.rjust(len_num," "),d.rjust(len_num," "))
        
        
def print_formatted(number):
    for i in range(1, number+1):
        x = len(bin(number)[2:])
        print(
            str(i).rjust(x), str(oct(i)[2:]).rjust(x), 
            (str(hex(i)[2:]).rjust(x)).upper(), str(bin(i)[2:]).rjust(x)
        
        )
