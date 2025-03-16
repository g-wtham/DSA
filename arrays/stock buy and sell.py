'''
Stock Buy And Sell

Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
min = select min from arr[]
max = select max ele
deduct max-min
'''

prices = [7,6,4,3,1]

def stock_buy(prices):
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            
        else:
            max_profit = max(max_profit, prices[i] - min_price)    
         
    return max_profit

print(stock_buy(prices))

'''
Logic :

1. Assume first element as minimum price, iteratively update the minimum price to the lowest value found so far.
2. To calc profit, if current price, prices[i] is more than min_price, it will go to `else` part and thus we assigned `min_price` as first value, 
   the current price which is `maximum` will be deducted from `min_price`.
3. The max_profit gets iteratively updated thus the maximum profit is obtained, since this only goes from 0 -> len(array), 
   it only counts for elements forward, thus, it doesnt mistakenly takes highest value which is behind the min_price index as higher, 
   since the selling date should be AFTER the  buying date, not in a circular fashion.
'''

