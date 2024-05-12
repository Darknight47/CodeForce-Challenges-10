import math
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    half = math.floor(n / 2)
    horiz = n
    ans = ((half - 1) * 4) + horiz
    print(ans)
    print("-----------")