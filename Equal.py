"""

--------------------- Link for the challenge: https://codeforces.com/problemset/problem/1931/B ----------------------------

There are n containers of water lined up, numbered from left to right from 1 to n. 
Each container can hold any amount of water; initially, the i-th container contains a(i) units of water. The sum of a(i) is divisible by n.

You can apply the following operation any (possibly zero) number of times: pour any amount of water from the i-th container to the j-th container, where i must be less than j (i.e. i< j). 
Any index can be chosen as i or j any number of times.

Determine whether it is possible to make the amount of water in all containers the same using this operation.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then the descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of containers with water.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 10^9) — the amounts of water in the containers. It is guaranteed that the sum of a(i) in each test case does not exceed 2⋅10^9. 
Also, the sum of a(i) is divisible by n.

It is guaranteed that the sum of n over all test cases in the input does not exceed 2⋅10^5.

Output
Output t lines, each of which is the answer to the corresponding test case. As the answer, output "YES" if it is possible to make the amount 
of water in all containers the same using the described operation. Otherwise, output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

Input:
6
1
43
2
1 3
5
4 5 2 1 3
3
1 2 3
7
4 5 5 0 6 4 4
7
6 5 5 1 3 4 4

Output:
YES
NO
YES
NO
NO
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    lstSum = sum(lst)
    equal = lstSum // sze
    barrel = 0
    ok = True
    for j in range(sze):
        temp = lst[j]
        if(temp > equal):
            barrel += (temp - equal)
        elif(temp < equal):
            diff = equal - temp
            if(barrel >= diff):
                barrel -= diff
            else:
                ok = False
                break
    print("YES" if ok else "NO")