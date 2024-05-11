"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1934/A ---------------------------

Given an array a of n elements, find the maximum value of the expression:

|ai−aj|+|aj−ak|+|ak−al|+|al−ai| where i, j, k, and l are four distinct indices of the array a, with 1 ≤ i, j , k , l ≤ n.

Here |x| denotes the absolute value of x.

Input
The first line contains one integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (4 ≤ n ≤ 100) — the length of the given array.

The second line of each test case contains n integers a1,a2,…,an (−10^6 ≤ a(i) ≤ 10^6).

Output
For each test case, print a single integer — the maximum value.

Input:
5
4
1 1 1 1
5
1 1 2 2 3
8
5 1 3 2 -3 -1 10 3
4
3 3 1 1
4
1 2 2 -1

Output:
0
6
38
8
8
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(list(map(int, input().split())))
    first = lst[0]
    second = lst[sze - 1]
    third = lst[sze - 2]
    fourth = lst[1]
    ans = abs(second - first) + abs(first - third) + abs(third - fourth) + abs(fourth - second)
    print(ans)