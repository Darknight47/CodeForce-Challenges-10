"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1971/B --------------------

You are given a string s consisting of lowercase English letters.

Rearrange the characters of s to form a new string r that is not equal to s, or report that it's impossible.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The only line of each test case contains a string s of length at most 10 consisting of lowercase English letters.

Output
For each test case, if no such string r exists as described in the statement, output "NO" (without quotes).

Otherwise, output "YES" (without quotes). Then, output one line — the string r, consisting of letters of string s.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes", and "Yes" will be recognized as a positive response).

If multiple answers are possible, you can output any of them.

Input:
8
codeforces
aaaaa
xxxxy
co
d
nutdealer
mwistht
hhhhhhhhhh

Output:
YES
forcodesec
NO
YES
xxyxx
YES
oc
NO
YES
undertale
YES
thtsiwm
NO
"""
cases = int(input())
for i in range(cases):
    s = input()
    tempSet = set(s)
    if(len(tempSet) == 1):
        print("NO")
    else:
        print("YES")
        if(s[::-1] == s):
            temp = list(s)
            for j in range(len(temp) - 1):
                first = temp[j]
                second = temp[j + 1]
                if(first != second):
                    temp[j + 1] = first
                    temp[j] = second
            print(''.join(temp))
        else:
            print(s[::-1])