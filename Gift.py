"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1862/A -----------------------

Recently, Tema and Vika celebrated Family Day. Their friend Arina gave them a carpet, which can be represented as an n⋅m table of lowercase Latin letters.

Vika hasn't seen the gift yet, but Tema knows what kind of carpets she likes. Vika will like the carpet if she can read her name on. She reads column by column from left to right 
and chooses one or zero letters from current column.

Formally, the girl will like the carpet if it is possible to select four distinct columns in order from left to right such that the first column contains "v", the second one contains "i", 
the third one contains "k", and the fourth one contains "a".

Help Tema understand in advance whether Vika will like Arina's gift.

Input
Each test consists of multiple test cases. The first line of input contains a single integer t
(1 ≤ t ≤ 100) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers n, m (1 ≤ n , m ≤ 20) — the sizes of the carpet.

The next n lines contain m lowercase Latin letters each, describing the given carpet.

Output
For each set of input data, output "YES" if Vika will like the carpet, otherwise output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.


Input:
5
1 4
vika
3 3
bad
car
pet
4 4
vvvv
iiii
kkkk
aaaa
4 4
vkak
iiai
avvk
viaa
4 7
vbickda
vbickda
vbickda
vbickda

Output:
YES
NO
YES
NO
YES
"""
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    arrHor = []
    for j in range(n):
        arrHor.append(input())
    arrVer = []
    for k in range(m):
        stemp = ""
        for s in arrHor:
            stemp += s[k]
        arrVer.append(stemp)
    vv = ii = kk = aa = ok = False
    for s in arrVer:
        if((not vv and not ii and not kk and not aa) and s.count('v') > 0):
            vv = True
        elif((vv and not ii and not kk and not aa) and s.count('i') > 0):
            ii = True
        elif((vv and ii and not kk and not aa) and s.count('k') > 0):
            kk = True
        elif((vv and ii and kk and not aa) and s.count('a') > 0):
            aa = True
    if(vv and ii and kk and aa):
        ok = True
    print("YES" if ok else "NO")