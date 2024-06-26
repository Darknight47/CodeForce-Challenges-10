"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1822/A ----------------------------------

Mushroom Filippov cooked himself a meal and while having his lunch, he decided to watch a video on TubeTube. He can not spend more than t seconds for lunch, so he asks you for help with the selection of video.

The TubeTube feed is a list of n videos, indexed from 1 to n. 
The i-th video lasts a(i) seconds and has an entertainment value b(i). 
Initially, the feed is opened on the first video, and Mushroom can skip to the next video in 1 second (if the next video exists). Mushroom can skip videos any number of times (including zero).

Help Mushroom choose one video that he can open and watch in tseconds. 
If there are several of them, he wants to choose the most entertaining one. Print the index of any appropriate video, or −1 if there is no such.

Input
The first line of the input data contains a single integer q (1 ≤ q ≤ 1000) — the number of test cases in the test.

The description of the test cases follows.

The first line of a test case contains two integers n and t (1 ≤ n ≤ 50, 1 ≤ t ≤ 200) — the number of videos in the feed and seconds for lunch, respectively.

The second line of a test case contains n integers a1,a2,a3,…,an (1 ≤ a(i) ≤ 100) — durations of videos.

The third line of a test case contains n integers b1,b2,b3,…,bn (1 ≤ b(i) ≤ 100) — entertainment values of videos.

Output
Output q integers, each of which is the answer to the corresponding test case. As an answer, output the index of the most entertaining video that Mushroom will have time to watch. 
If there are several answers, you are allowed to output any of them. 
Output −1, if there is no video he can watch during his lunch break.

Input:
5
5 9
1 5 7 6 6
3 4 7 1 9
4 4
4 3 3 2
1 2 3 4
5 7
5 5 5 5 5
2 1 3 9 7
4 33
54 71 69 96
42 24 99 1
2 179
55 66
77 88

Output:
3
2
3
-1
2
"""
cases = int(input())
for i in range(cases):
    sze, t = map(int, input().split())
    durations = list(map(int, input().split()))
    entertainments = list(map(int, input().split()))
    best = -1
    founded = False
    ans = 0
    for j in range(sze):
        dur = durations[j]
        ent = entertainments[j]
        if(t >= dur):
            if(best < ent):
                best = ent
                ans = j + 1
                founded = True
        t -= 1
    print(ans if founded else -1)