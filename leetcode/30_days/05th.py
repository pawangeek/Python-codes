# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Topic - Greedy

prices = [7,1,5,2,3,6]
profit_from_price = 0
        
for i in range(len(prices)-1):

    # check next maxima in array and add prices till that       
    if prices[i]<prices[i+1]:
        profit_from_price += prices[i+1]-prices[i]
                
print(profit_from_price)