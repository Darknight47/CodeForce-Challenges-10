"""

-------------------- Link for the challenge: https://codeforces.com/problemset/problem/1741/A ------------------------------

Two T-shirt sizes are given: a and b. 
The T-shirt size is either a string M or a string consisting of several (possibly zero) characters X and one of the characters S or L.

For example, strings M, XXL, S, XXXXXXXS could be the size of some T-shirts. And the strings XM, LL, SX are not sizes.

The letter M stands for medium, S for small, L for large. The letter X refers to the degree of size (from eXtra). 
For example, XXL is extra-extra-large (bigger than XL, and smaller than XXXL).

You need to compare two given sizes of T-shirts a and b.

The T-shirts are compared as follows:

any small size (no matter how many letters X) is smaller than the medium size and any large size;
any large size (regardless of the number of letters X) is larger than the medium size and any small size;
the more letters X before S, the smaller the size;
the more letters X in front of L, the larger the size.
For example:

XXXS < XS
XXXL > XL
XL > M
XXL = XXL
XXXXXS < M
XL > XXXS

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of one line, in which a and b T-shirt sizes are written. The lengths of the strings corresponding to the T-shirt sizes do not exceed 50. 
It is guaranteed that all sizes are correct.

Output
For each test case, print on a separate line the result of comparing a and b T-shirt sizes (lines "<", ">" or "=" without quotes).


Input:
6
XXXS XS
XXXL XL
XL M
XXL XXL
XXXXXS M
L M

Output:
<
>
>
=
<
>
"""
cases = int(input())
for i in range(cases):
    t1, t2 = input().split()
    t1x = t1.count('X')
    t2x = t2.count('X')
    if(t1[-1] == 'L' and (t2[-1] == 'M' or t2[-1] == 'S')):
        print(">")
    elif(t1[-1] == 'L' and t2[-1] == 'L'):
        if(t1x > t2x):
            print(">")
        elif(t1x < t2x):
            print("<")
        else:
            print("=")
    if(t1[-1] == 'M' and t2[-1] == 'S'):
        print(">")
    elif(t1[-1] == 'M' and t2[-1] == 'L'):
        print("<")
    elif(t1[-1] == 'M' and t2[-1] == 'M'):
        if(t1x > t2x):
            print(">")
        elif(t1x < t2x):
            print("<")
        else:
            print("=")
    if(t1[-1] == 'S' and (t2[-1] == 'M' or t2[-1] == 'L')):
        print("<")
    elif(t1[-1] == 'S' and t2[-1] == 'S'):
        if(t1x > t2x):
            print("<")
        elif(t1x < t2x):
            print(">")
        else:
            print("=")