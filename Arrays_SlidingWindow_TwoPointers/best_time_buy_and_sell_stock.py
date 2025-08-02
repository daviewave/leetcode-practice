# Time: 
# Space:
#-
# 
# 
# 

def best_time_buy_and_sell_stock(prices):
    if not prices or len(prices) < 2:
        return 0
    
    min_price, best_profit = prices[0], 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])  # always track lowest price so far
        todays_profit = prices[i] - min_price
        best_profit = max(best_profit, todays_profit)

        
        

if __name__ == "__main__":
    best_time_buy_and_sell_stock()