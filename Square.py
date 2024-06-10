"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1921/A --------------------------

A square of positive (strictly greater than 0) area is located on the coordinate plane, with sides parallel to the coordinate axes. 
You are given the coordinates of its corners, in random order. Your task is to find the area of the square.

Input
Each test consists of several testcases. The first line contains one integer t (1 ≤ t ≤ 100) — the number of testcases. The following is a description of the testcases.

Each testcase contains four lines, each line contains two integers x(i), y(i) (−1000 ≤ x(i) , y(i) ≤ 1000), coordinates of the corners of the square.

It is guaranteed that there is a square with sides parallel to the coordinate axes, with positive (strictly greater than 0) area, with corners in given points.

Output
For each test case, print a single integer, the area of the square.

Input:
3
1 2
4 5
1 5
4 2
-1 1
1 -1
1 1
-1 -1
45 11
45 39
17 11
17 39

Output:
9
4
784
"""

cases = int(input())
for i in range(cases):
    xMin = 2000 
    xMax = -2000
    for j in range(4):
        x, y = map(int, input().split())
        if(x < xMin):
            xMin = x
        if(x > xMax):
            xMax = x
    print(abs(xMax - xMin) ** 2)