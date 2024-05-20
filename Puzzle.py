"""

--------------------- Link for the challenge: https://codeforces.com/problemset/problem/1933/A -----------------------

You are given an array a of n integers. You must perform the following two operations on the array (the first, then the second):

Arbitrarily rearrange the elements of the array or leave the order of its elements unchanged.
Choose at most one contiguous segment of elements and replace the signs of all elements in this segment with their opposites. Formally, you can choose a pair of indices l,r
such that 1≤l≤r≤n and assign ai=−ai for all l≤i≤r (negate elements). 
Note that you may choose not to select a pair of indices and leave all the signs of the elements unchanged.
What is the maximum sum of the array elements after performing these two operations (the first, then the second)?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the number of elements in array a.

The second line of each test case contains n integers a1,a2,…,an (−100 ≤ a(i) ≤ 100) — elements of the array.

Output
For each test case, output the maximum sum of the array elements after sequentially performing the two given operations.

Input:
8
3
-2 3 -3
1
0
2
0 1
1
-99
4
10 -2 -3 7
5
-1 -2 -3 -4 -5
6
-41 22 -69 73 -15 -50
12
1 2 3 4 5 6 7 8 9 10 11 12

Output:
8
0
1
99
22
15
270
78
"""
cases = int(input())
for i in range(cases):
    input()
    print(sum(list(map(abs, map(int, input().split())))))