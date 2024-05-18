"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1660/B ---------------------------------

Not so long ago, Vlad had a birthday, for which he was presented with a package of candies. There were n types of candies, there are a(i) candies of the type i (1 ≤ i ≤ n).

Vlad decided to eat exactly one candy every time, choosing any of the candies of a type that is currently the most frequent 
(if there are several such types, he can choose any of them). To get the maximum pleasure from eating, Vlad does not want to eat two candies of the same type in a row.

Help him figure out if he can eat all the candies without eating two identical candies in a row.

Input
The first line of input data contains an integer t (1 ≤ t ≤ 10^4) — the number of input test cases.

The following is a description of t test cases of input, two lines for each.

The first line of the case contains the single number n ( 1 ≤ n ≤ 2⋅10^5) — the number of types of candies in the package.

The second line of the case contains n integers a(i) (1 ≤ a(i) ≤ 10^9) — the number of candies of the type i.

It is guaranteed that the sum of n for all cases does not exceed 2⋅10^5.

Output
Output t lines, each of which contains the answer to the corresponding test case of input. As an answer, output "YES" if Vlad can eat candy as planned, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Input:
6
2
2 3
1
2
5
1 6 2 4 3
4
2 2 2 1
3
1 1000000000 999999999
1
1

Output:
YES
NO
NO
YES
YES
YES
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(list(map(int, input().split())))
    if(sze == 1 and lst[0] > 1):
        print("NO")
    elif(sze == 1 and lst[0] == 1):
        print("YES")
    else:
        if(lst[sze - 2] + 1 < lst[sze - 1]):
            print("NO")
        else:
            print("YES")