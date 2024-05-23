"""

-------------------- Link for the challenge: https://codeforces.com/problemset/problem/1919/B ------------------------

You are given a string s of length n consisting of characters "+" and "-". s represents an array a of length n defined by ai=1 if si= "+" and ai=−1 if si= "-".

You will do the following process to calculate your penalty:

Split a into non-empty arrays b1,b2,…,bk such that b1+b2+…+bk=a†, where + denotes array concatenation.

The penalty of a single array is the absolute value of its sum multiplied by its length. In other words, for some array c
of length m, its penalty is calculated as p(c)=|c1+c2+…+cm|⋅m.
The total penalty that you will receive is p(b1)+p(b2)+…+p(bk).

If you perform the above process optimally, find the minimum possible penalty you will receive.

† Some valid ways to split a=[3,1,4,1,5] into (b1,b2,…,bk) are ([3],[1],[4],[1],[5]), ([3,1],[4,1,5]) and ([3,1,4,1,5]) while some invalid ways to split a are 
([3,1],[1,5]), ([3],[],[1,4],[1,5]) and ([3,4],[5,1,1]).

Input
Each test contains multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 5000) — the length of string s.

The second line of each test case contains string s (si∈{+,−}, |s|=n).

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, output a single integer representing the minimum possible penalty you will receive


Input:
5
1
+
5
-----
6
+-+-+-
10
--+++++++-
20
+---++++-+++++---++-

Output:
1
5
0
4
4
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    plus = s.count('+')
    minus = s.count('-')
    print(abs(plus - minus))