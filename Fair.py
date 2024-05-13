"""

------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1472/B ----------------------

Alice and Bob received n candies from their parents. Each candy weighs either 1 gram or 2 grams. Now they want to divide all candies 
among themselves fairly so that the total weight of Alice's candies is equal to the total weight of Bob's candies.

Check if they can do that.

Note that candies are not allowed to be cut in half.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then t test cases follow.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the number of candies that Alice and Bob received.

The next line contains n integers a1,a2,…,an — the weights of the candies. The weight of each candy is either 1 or 2.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output on a separate line:

"YES", if all candies can be divided into two sets with the same weight;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).

Input:
5
2
1 1
2
1 2
4
1 2 1 2
3
2 2 2
3
2 1 2

Output:
YES
NO
YES
NO
NO
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    candySums = sum(lst)
    if(candySums % 2 == 1):
        print("NO")
    else:
        ones = 0
        twos = 0
        for j in lst:
            if(j == 1):
                ones += 1
            else:
                twos += 1
        if(candySums % 2 == 0 and ones >= 2):
            print("YES")
        elif(candySums % 2 == 0 and ones == 0 and sze % 2 == 0):
            print("YES")
        else:
            print("NO")