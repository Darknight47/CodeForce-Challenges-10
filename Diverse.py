"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/988/A ---------------------

There are n students in a school class, the rating of the i-th student on Codehorses is a(i). 
You have to form a team consisting of k students (1 ≤ k ≤ n) such that the ratings of all team members are distinct.

If it is impossible to form a suitable team, print "NO" (without quotes). Otherwise print "YES", and then print k
distinct numbers which should be the indices of students in the team you form. If there are multiple answers, print any of them.

Input
The first line contains two integers n and k (1 ≤ k ≤ n ≤ 100) — the number of students and the size of the team you have to form.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100), where a(i) is the rating of i-th student.

Output
If it is impossible to form a suitable team, print "NO" (without quotes). Otherwise print "YES", and then print k distinct integers from 1 to n which should be the 
indices of students in the team you form. All the ratings of the students in the team should be distinct. You may print the indices in any order. 
If there are multiple answers, print any of them.

Assume that the students are numbered from 1 to n.

Input:
5 3
15 13 15 15 12

Output:
YES
1 2 5 
"""
n, k = map(int, input().split())
lst = list(map(int, input().split()))
tempLst = []
ans = []
for i in range(n):
    temp = lst[i]
    if(temp not in tempLst):
        tempLst.append(temp)
        ans.append(i + 1)
    if(len(ans) == k):
        break
if(len(ans) == k):
    print("YES")
    print(*ans)
else:
    print("NO")