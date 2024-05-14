"""

----------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1856/A ---------------------------

Alphen has an array of positive integers a of length n.

Alphen can perform the following operation:

For all i from 1 to n, replace a(i) with max(0,ai−1).
Alphen will perform the above operation until a is sorted, that is a satisfies a1 ≤ a2 ≤ … ≤ an. 
How many operations will Alphen perform? Under the constraints of the problem, it can be proven that Alphen will perform a finite number of operations.

Input
Each test contains multiple test cases. The first line of input contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 50) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the array a.

Output
For each test case, output a single integer — the number of operations that Alphen will perform.

Input:
7
3
1 2 3
5
2 1 2 1 2
4
3 1 5 4
2
7 7
5
4 1 3 2 5
5
2 3 1 4 5
3
1000000000 1 2

Output:
0
2
5
0
4
3
1000000000
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    biggest = 0
    for j in range(sze - 1, 0, -1):
        first = lst[j]
        second = lst[j - 1]
        if(second > first):
            if(second > biggest):
                biggest = second
    print(biggest)