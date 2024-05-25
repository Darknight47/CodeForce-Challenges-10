"""

----------------------- Link for the challenge: https://codeforces.com/contest/1312/problem/B ----------------------------

You are given an array a1,a2,…,an. Array is good if for each pair of indexes i < j the condition j−aj ≠ i−ai holds. 
Can you shuffle this array so that it becomes good? To shuffle an array means to reorder its elements arbitrarily (leaving the initial order is also an option).

For example, if a=[1,1,3,5], then shuffled arrays [1,3,5,1], [3,5,1,1] and [5,3,1,1] are good, but shuffled arrays [3,1,5,1], [1,1,3,5] and [1,1,5,3] aren't.

It's guaranteed that it's always possible to shuffle an array to meet this condition.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains one integer n (1 ≤ n ≤ 100) — the length of array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100).

Output
For each test case print the shuffled version of the array a which is good.

Input:
3
1
7
4
1 1 3 5
6
3 2 1 5 6 4

Output:
7
1 5 1 3
2 4 6 1 3 5
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(list(map(int, input().split())))
    lstRev = reversed(lst)
    print(*lstRev)