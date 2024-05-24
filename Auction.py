"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1454/B -------------------------------

There is a game called "Unique Bid Auction". You can read more about it here: https://en.wikipedia.org/wiki/Unique_bid_auction (though you don't have to do it to solve this problem).

Let's simplify this game a bit. Formally, there are nparticipants, the i-th participant chose the number a(i). 
The winner of the game is such a participant that the number he chose is unique (i. e. nobody else chose this number except him) and is minimal (i. e. among all unique values of a the minimum one is the winning one).

Your task is to find the index of the participant who won the game (or -1 if there is no winner). Indexing is 1-based, i. e. the participants are numbered from 1 to n.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 2⋅10^4) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (1 ≤ n ≤ 2⋅10^5) — the number of participants. 
The second line of the test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ n), where a(i) is the i-th participant chosen number.

It is guaranteed that the sum of n does not exceed 2⋅10^5 (∑n ≤ 2⋅10^5).

Output
For each test case, print the answer — the index of the participant who won the game (or -1 if there is no winner). Note that the answer is always unique.

Input:
6
2
1 1
3
2 1 3
4
2 2 2 3
1
1
5
2 3 2 4 2
6
1 1 5 5 4 4

Output:
-1
2
4
1
2
-1
"""
cases = int(input())
for i in range(cases):
    n = int(input())
    lst = list(map(int, input().split()))
    diction = {}
    for num in lst:
        if(num in diction):
            diction[num] += 1
        else:
            diction[num] = 1
    tempMin = 500000
    ok = False
    for j in diction:
        tv = diction[j]
        if(tv == 1):
            if(j < tempMin):
                tempMin = j
                ok = True
    if(ok):
        print(lst.index(tempMin) + 1)
    else:
        print(-1)