"""

------------------ Link for the challenge: https://codeforces.com/problemset/problem/1984/A ----------------------

Define the range of a non-empty array to be the maximum value minus the minimum value. For example, the range of [1,4,2] is 4−1=3.

You are given an array a1,a2,…,an of length n ≥ 3. It is guaranteed a is sorted.

You have to color each element of a red or blue so that:

the range of the red elements does not equal the range of the blue elements, and
there is at least one element of each color.
If there does not exist any such coloring, you should report it. If there are multiple valid colorings, you can print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains an integer n (3 ≤ n ≤ 50) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9). It is guaranteed a1≤a2≤…≤an−1≤an.

Output
For each test case, if it is impossible to color a to satisfy all the constraints, output NO.

Otherwise, first output YES.

Then, output a string s of length n. 
For 1 ≤ i ≤ n, if you color a(i) red, s(i) should be R. For 1 ≤ i ≤ n, if you color a(i) blue, s(i) should be B.

Input:
7
4
1 1 2 2
5
1 2 3 4 5
3
3 3 3
4
1 2 2 2
3
1 2 2
3
1 1 2
3
1 9 84

Output:
YES
RBRR
YES
BBRBB
NO
YES
RBBR
YES
RRB
YES
BRR
YES
BRB
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    if(arr[0] == arr[sze - 1]):
        print("NO")
    else:
        ans = "RB"
        for j in range(sze - 2):
            ans += "R"
        print("YES")
        print(ans)