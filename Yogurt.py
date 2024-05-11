"""

-------------- Link for the challenge: https://codeforces.com/problemset/problem/1955/A --------------------------

The price of one yogurt at the "Vosmiorochka" store is a burles, but there is a promotion where you can buy two yogurts for b burles.

Maxim needs to buy exactly n yogurts. When buying two yogurts, he can choose to buy them at the regular price or at the promotion price.

What is the minimum amount of burles Maxim should spend to buy n yogurts?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first and only line of each test case contains three integers n, a, and b (1 ≤ n ≤ 100, 1 ≤ a, b ≤ 30) — the number of yogurts Maxim wants to buy, 
the price for one yogurt, and the price for two yogurts on promotion.

Output
For each test case, print in a separate line the minimum cost of buying n yogurts at "Vosmiorochka".

Input:
4
2 5 9
3 5 9
3 5 11
4 5 11

Output:
9
14
15
20
"""
cases = int(input())
for i in range(cases):
    n, a, b = map(int, input().split())
    buySingles = n * a
    if(n % 2 == 0):
        buyDoubles = (n // 2) * b
    else:
        temp = n - 1
        buyDoubles = ((temp // 2) * b) + a
    print(min(buySingles, buyDoubles))