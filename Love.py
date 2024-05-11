"""

--------------------------- Link for the challenge: https://codeforces.com/contest/1539/problem/B -------------------------

Petya once wrote a sad love song and shared it to Vasya. The song is a string consisting of lowercase English letters. Vasya made up q
questions about this song. Each question is about a subsegment of the song starting from the l-th letter to the r-th letter. 
Vasya considers a substring made up from characters on this segment and repeats each letter in the subsegment k times, where k is the index of the corresponding letter in the alphabet. 
For example, if the question is about the substring "abbcb", then Vasya repeats letter 'a' once, each of the letters 'b' twice, letter 'c" three times, so that the resulting string 
is "abbbbcccbb", its length is 10. 
Vasya is interested about the length of the resulting string.

Help Petya find the length of each string obtained by Vasya.

Input
The first line contains two integers n and q (1 ≤ n ≤ 100000, 1 ≤ q ≤ 100000) — the length of the song and the number of questions.

The second line contains one string s — the song, consisting of n lowercase letters of English letters.

Vasya's questions are contained in the next q lines. Each line contains two integers l and r (1 ≤ l ≤ r ≤ n) — the bounds of the question.

Output
Print q lines: for each question print the length of the string obtained by Vasya.

Input:
7 3
abacaba
1 3
2 5
1 7

Output:
4
7
11
"""
sze, questions = map(int, input().split())
song = input()
# Preprocess the string to calculate the prefix sum array
# The array is the sum of the numbers of letters up to that point in the string.
prefix_sum = [0]
for char in song:
    prefix_sum.append(prefix_sum[-1] + (ord(char) - 96 if char.isalpha() else 0))
# Answer each question using the prefix sum array
for i in range(questions):
    l, r = map(int, input().split())
    l -= 1
    # Calculating the sum of the numbers of letters in the substring by subtracting the prefix sum at the start of the substring from the prefix sum at the end of the substring.
    ans = prefix_sum[r] - prefix_sum[l]
    print(ans)