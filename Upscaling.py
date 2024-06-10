"""
You are given an integer n. Output a 2n×2n checkerboard made of 2×2 squares alternating '#' and '.', with the top-left cell being '#'.

Input
The first line contains an integer t (1 ≤ t ≤ 20) — the number of test cases.

The only line of each test case contains a single integer n (1 ≤ n ≤ 20) — it means you need to output a checkerboard of side length 2n.

Output
For each test case, output 2n lines, each containing 2n characters without spaces — the checkerboard, as described in the statement. Do not output empty lines between test cases.

Input:
4
1
2
3
4

Output:
##
##
##..
##..
..##
..##
##..##
##..##
..##..
..##..
##..##
##..##
##..##..
##..##..
..##..##
..##..##
##..##..
##..##..
..##..##
..##..##
"""
cases = int(input())
for i in range(cases):
    n = int(input())
    arr = []
    for j in range(n):
        if(j % 2 == 0 ):
            hasht = True
        else:
            hasht = False
        temp = ""
        for k in range(n):
            if(hasht):
                temp += "##"
                hasht = False
            else:
                temp += ".."
                hasht = True
        arr.append(temp)
        arr.append(temp)
    for p in arr:
        print(p)