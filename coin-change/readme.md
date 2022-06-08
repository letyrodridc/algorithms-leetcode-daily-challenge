## 322. Coin Change

This is the classical coin change problem but solved with Dynamic Programming.

It's a Bottom-Up solution using an array with size equal to amount as memorization. 

The complexity of the algorithm will be O(m\*n) being n the amount of change and m the different coin 
denominations.

In terms of implementation, the elegance of this solution is to iterate between coin denominations that could be an small amount. It corresponds to point out that this statement doesn't mean the the same as thinking it in theory. From a theoretical perspective, coins denominations set can be as big as possible.

The idea is:
1. Create an array of size amount. Initialize it values in -1
2. Complete the array with 1s in the possitions that match with denomination. This means, how many coins of 5 we need using a coin of 5 denomination? It's just 1. So we are going to fill up those initial cases. 
3. Iterate the amount array from start to end and in each index verify if exists a combination of coins we can use to sum-up the current amount (index).
For doing that, we iterate all coin denominations. For each one, we check the current coin denomination and index-coin array positions grater are -1. If that's true, we sum both values and we will get the total number of coins needed for the current amount. If this value the minimum we had found so far, we will update the amount array.

Problem source: https://leetcode.com/problems/coin-change

Check Solution.py file to see the Python implementation.
