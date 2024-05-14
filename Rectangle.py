"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1622/A -------------------

There are three sticks with integer lengths l1,l2 and l3.

You are asked to break exactly one of them into two pieces in such a way that:

both pieces have positive (strictly greater than 0) integer length;
the total length of the pieces is equal to the original length of the stick;
it's possible to construct a rectangle from the resulting four sticks such that each stick is used as exactly one of its sides.
A square is also considered a rectangle.

Determine if it's possible to do that.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The only line of each testcase contains three integers l1,l2,l3 (1 ≤ l(i) ≤ 10^8) — the lengths of the sticks.

Output
For each testcase, print "YES" if it's possible to break one of the sticks into two pieces with positive integer length in such a way that it's 
possible to construct a rectangle from the resulting four sticks. Otherwise, print "NO".

You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES are all recognized as a positive answer).

Input:
4
6 1 5
2 5 2
2 4 2
5 5 4

Output:
YES
NO
YES
YES
"""
cases = int(input())
for i in range(cases):
    a, b, c = map(int, input().split())
    if((a + b) == c or(a + c) == b or (b + c) == a):
        print("YES")
    elif((a == b and c % 2 == 0) or (a == c and b % 2 == 0) or (b == c and a % 2 == 0)):
        print("YES")
    else:
        print("NO")