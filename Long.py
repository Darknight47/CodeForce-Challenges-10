"""

------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1843/B ----------------------------

Today Alex was brought array a1,a2,…,an of length n. 
He can apply as many operations as he wants (including zero operations) to change the array elements.

In 1 operation Alex can choose any l and r such that 1 ≤ l ≤ r ≤ n, and multiply all elements of the array from l to r inclusive by −1. 
In other words, Alex can replace the subarray [al,al+1,…,ar] by [−al,−al+1,…,−ar] in 1 operation.

For example, let n=5, the array is [1,−2,0,3,−1], l=2 and r=4, then after the operation the array will be [1,2,0,−3,−1].

Alex is late for school, so you should help him find the maximum possible sum of numbers in the array, which can be obtained by making any number of operations, 
as well as the minimum number of operations that must be done for this.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — number of test cases. Then the descriptions of the test cases follow.

The first line of each test case contains one integer n (1 ≤ n ≤ 2⋅10^5) — length of the array.

The second line contains n integers a1,a2,…,an (−10^9 ≤ a(i) ≤ 10^9) — elements of the array.

It is guaranteed that the sum of n for all test cases does not exceed 2⋅10^5.

Output
For each test case output two space-separated numbers: the maximum possible sum of numbers in the array and the minimum number of operations to get this sum.

Pay attention that an answer may not fit in a standard integer type, so do not forget to use 64-bit integer type.

Input:
5
6
-1 7 -4 -2 5 -8
8
-1 0 0 -2 1 0 -3 0
5
2 -1 0 -3 -7
5
0 -17 0 1 0
4
-1 0 -2 -1

Output:
27 3
7 2
13 1
18 1
4 1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    minReq = 0
    ans = 0
    tempReq = 0
    seen = False
    for num in lst:
        if(num < 0 and not seen):
            tempReq += 1
            seen = True
        elif(num > 0):
            seen = False
            minReq += tempReq
            tempReq = 0
        ans += abs(num)
    if(tempReq == 1):
        minReq += 1
    print(ans, minReq)