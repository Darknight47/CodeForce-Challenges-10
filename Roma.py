"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/262/A ------------------------

Roma (a popular Russian name that means 'Roman') loves the Little Lvov Elephant's lucky numbers.

Let us remind you that lucky numbers are positive integers whose decimal representation only contains lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Roma's got n positive integers. He wonders, how many of those integers have not more than k lucky digits? Help him, write the program that solves the problem.

Input
The first line contains two integers n, k (1 ≤ n, k ≤ 100). The second line contains n integers ai (1 ≤ ai ≤ 10^9) — the numbers that Roma has.

The numbers in the lines are separated by single spaces.

Output
In a single line print a single integer — the answer to the problem.

Input:
3 4
1 2 4

Output:
3
"""
n, k = map(int, input().split())
lst = map(int, input().split())
ans = 0
for num in lst:
    tmpCount = 0
    while num > 0:
        dig = num % 10
        num //= 10
        if(dig == 4 or dig == 7):
            tmpCount += 1
    if(tmpCount <= k):
        ans += 1
print(ans)