"""

-------------- Link for the challenge: https://codeforces.com/problemset/problem/1385/A --------------------

You are given three positive (i.e. strictly greater than zero) integers x, y and z.

Your task is to find positive integers a, b and c such that x=max(a,b), y=max(a,c) and z=max(b,c) , or determine that it is impossible to find such a, b and c.

You have to answer t independent test cases. Print required a, b and c in any (arbitrary) order.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 2⋅10^4) — the number of test cases. Then t test cases follow.

The only line of the test case contains three integers x, y, and z (1 ≤ x, y, z ≤ 10^9).

Output
For each test case, print the answer:

"NO" in the only line of the output if a solution doesn't exist; 
or "YES" in the first line and any valid triple of positive integers a, b and c ( 1 ≤ a, b, c ≤ 10^9) in the second line. You can print a, b and c in any order.

Input:
5
3 2 3
100 100 100
50 49 49
10 30 20
1 1000000000 1000000000

Output:
YES
3 2 1
YES
100 100 100
NO
NO
YES
1 1 1000000000
"""
cases = int(input())
for i in range(cases):
    x, y, z = sorted(map(int, input().split()))  # Sort the input values
    if y != z:  # If the two largest values are not equal, it's impossible
        print("NO")
    else:  # Otherwise, it's possible and a, b, c are x, x, and z respectively
        print("YES")
        print(x, x, z)