## 121. Best Time to Buy and Sell Stock

Solved with Dynamic Programming

The idea is to keep track of the max profit so far by day. So, we will create a array of n days (being n the len of prices).

The first day (day=0) the profit is going to be 0. Then, we are going to select the profit from the maximum between the previous day and the current day price - buying price.

The other important thing is to keep track of the buying price. Due that prices are all positives, we can always keep the minior price seen so far as the best buying price.

Check the Solution.py file for the implementation in Python.

Problem statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
