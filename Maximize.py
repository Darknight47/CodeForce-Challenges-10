"""

-------------- Link for the challenge: https://codeforces.com/problemset/problem/1968/A ------------------

You are given an integer x. Your task is to find any integer y (1 ≤ y < x) such that gcd(x,y)+y is maximum possible.

Note that if there is more than one y which satisfies the statement, you are allowed to find any.

gcd(a,b) is the Greatest Common Divisor of a and b. For example, gcd(6,4)=2.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each of the following t lines contains a single integer x (2 ≤ x ≤ 1000).

Output
For each test case, output any y (1 ≤ y < x), which satisfies the statement.

Input:
7
10
7
21
100
2
1000
6

Output:
5
6
18
98
1
750
3
"""

cases = int(input())
for i in range(cases):
    x = int(input())
    print(x - 1)