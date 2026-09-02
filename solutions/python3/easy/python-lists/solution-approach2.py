# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 09:24 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        name, *line = input().split()
        line = list(map(int, line))
        if len(line) <= 2:
            if name == "insert":
                list1.insert(line[0],line[1])
            elif name == "print":
                print(list1)
            elif name == "remove":
                list1.remove(line[0])
            elif name == "append":
                list1.append(line[0])
            elif name == "sort":
                list1.sort()
            elif name == "pop":
                list1.pop()
            elif name == "reverse":
                list1.reverse()
