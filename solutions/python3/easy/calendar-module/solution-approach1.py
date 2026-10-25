# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Problem     Calendar Module
# Difficulty  Easy
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-25, 11:05 a.m.
# ──────────────────────────────────────────────────

import calendar

month, day, year = [int(x) for x in input().split()]
day_num = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_num]

print(day_name.upper())
