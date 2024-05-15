"""

----------------------- Link for the challenge: https://codeforces.com/contest/835/problem/B --------------------------

Some natural number was written on the board. Its sum of digits was not less than k. But you were distracted a bit, and someone changed this number to n, 
replacing some digits with others. It's known that the length of the number didn't change.

You have to find the minimum number of digits in which these two numbers can differ.

Input
The first line contains integer k (1 ≤ k ≤ 109).

The second line contains integer n (1 ≤ n < 10100000).

There are no leading zeros in n. It's guaranteed that this situation is possible.

Output
Print the minimum number of digits in which the initial number and n can differ.

Input:
3
11

Output:
1
"""
k = int(input())
strNum = input()
sortedNums = sorted(strNum)
currSum = sum(int(dig) for dig in sortedNums)
ans = 0
for dig in sortedNums:
    if currSum < k:
        currSum += 9 - int(dig)
        ans += 1
print(ans)