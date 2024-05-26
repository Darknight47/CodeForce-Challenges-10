"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1950/C --------------------------------

Given the time in 24-hour format, output the equivalent time in 12-hour format.

24-hour format divides the day into 24 hours from 00 to 23, each of which has 60 minutes from 00 to 59.
12-hour format divides the day into two halves: the first half is AM, and the second half is PM. 
In each half, the hours are numbered in the order 12,01,02,03,…,11. 
Each hour has 60 minutes numbered from 00 to 59.

Input
The first line contains a single integer t (1 ≤ t ≤ 1440) — the number of test cases.

The only line of each test case contains a string s of length 5 with format hh:mm representing a valid time in the 24-hour format. 
hh represents the hour from 00 to 23, and mm represents the minute from 00 to 59.

The input will always be a valid time in 24-hour format.

Output
For each test case, output two strings separated by a space ("hh:mm AM" or "hh:mm PM"), which are the 12-hour equivalent to the time provided in the test case (without quotes).

You should output the time exactly as indicated; in particular, you should not remove leading zeroes.

Input:
11
09:41
18:06
12:14
00:59
00:00
14:34
01:01
19:07
11:59
12:00
21:37

Output:
09:41 AM
06:06 PM
12:14 PM
12:59 AM
12:00 AM
02:34 PM
01:01 AM
07:07 PM
11:59 AM
12:00 PM
09:37 PM
"""
cases = int(input())
for i in range(cases):
    s = input()
    temp = s.split(":")
    hour = int(temp[0])
    minutes = int(temp[1])
    half = ""
    if(hour < 12):
        if(hour == 0):
            hour = 12
        half = "AM"
    else:
        if(hour > 12):
            hour -= 12
        half = "PM"
    if(hour < 10 and minutes < 10):
        print(f'0{hour}:0{minutes} {half}')
    elif(hour < 10 and minutes >= 10):
        print(f'0{hour}:{minutes} {half}')
    elif(hour >= 10 and minutes < 10):
        print(f'{hour}:0{minutes} {half}')
    else:
        print(f'{hour}:{minutes} {half}')