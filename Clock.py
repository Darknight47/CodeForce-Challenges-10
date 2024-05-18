"""

----------------- Link for the challenge: https://codeforces.com/problemset/problem/1971/C -----------------------

There is a clock labeled with the numbers 1 through 12 in clockwise order, as shown below.
Alice and Bob have four distinct integers a, b, c, d not more than 12. Alice ties a red string connecting a and b, and Bob ties a blue string connecting c and d. 
Do the strings intersect? (The strings are straight line segments.)

Input
The first line contains a single integer t (1 ≤ t ≤ 5940) — the number of test cases.

The only line of each test case contains four distinct integers a, b, c, d (1≤a,b,c,d≤12).

Output
For each test case, output "YES" (without quotes) if the strings intersect, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes", and "Yes" will be recognized as a positive response).

Input:
15
2 9 10 6
3 8 9 1
1 2 3 4
5 3 4 12
1 8 2 10
3 12 11 8
9 10 12 1
12 1 10 2
3 12 6 9
1 9 8 4
6 7 9 12
7 12 9 6
10 12 11 1
3 9 6 12
1 4 3 5

Output:
YES
NO
NO
YES
YES
NO
NO
NO
NO
NO
NO
YES
YES
YES
YES
"""
def check_intersect(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c

    if a < c < b and b < d:
        return "YES"
    elif a < d < b and b < c:
        return "YES"
    elif c < a < d and d < b:
        return "YES"
    elif c < b < d and d < a:
        return "YES"
    else:
        return "NO"

cases = int(input())
for i in range(cases):
    a, b, c, d = map(int, input().split())
    print(check_intersect(a, b, c, d))