"""

------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1969/A ----------------------------

Monocarp wants to throw a party. He has n friends, and he wants to have at least 2 of them at his party.

The i-th friend's best friend is p(i). All p(i) are distinct, and for every i ∈ [1,n], p(i)≠i.

Monocarp can send invitations to friends. 
The i-th friend comes to the party if both the i-th friend and the p(i)-th friend receive an invitation (note that the p(i)-th friend doesn't have to actually come to the party). 
Each invitation is sent to exactly one of the friends.

For example, if p=[3,1,2,5,4], and Monocarp sends invitations to the friends [1,2,4,5], then the friends [2,4,5] will come to the party. 
The friend 1 won't come since his best friend didn't receive an invitation; the friend 3 won't come since he didn't receive an invitation.

Calculate the minimum number of invitations Monocarp has to send so that at least 2 friends come to the party.

Input
The first line contains one integer t (1 ≤ t ≤ 5000) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n (2 ≤ n ≤ 50) — the number of friends;
the second line contains n integers p1,p2,…,pn (1 ≤ p(i) ≤ n; p(i) ≠ i; 
all p(i) are distinct).

Output
Print one integer — the minimum number of invitations Monocarp has to send.


Input:
3
5
3 1 2 5 4
4
2 3 4 1
2
2 1

Output:
2
3
2
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    two = False
    for j in range(sze):
        first = lst[j]
        firstFriend = lst[first - 1]
        firstFiendsFriend = lst[firstFriend - 1]
        if(first == firstFiendsFriend):
            two = True
            break
    print(2 if two else 3)