###Stock Transaction Program

### Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
### purchase:
# The number of shares that Joe purchased was 2,000.
# When Joe purchased the stock, he paid $40.00 per share.
# Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
# for the stock.

### Two weeks later, Joe sold the stock. Here are the details of the sale:
# The number of shares that Joe sold was 2,000.
# He sold the stock for $42.75 per share.
# He paid his stockbroker another commission that amounted to 3 percent of the amount
# he received for the stock.

### Write a program that displays the following information:
# The amount of money Joe paid for the stock.
# The amount of commission Joe paid his broker when he bought the stock.
# The amount for which Joe sold the stock.

#Named Constants
STOCK_QUANTITY = 2000.00
STOCK_COMMISSION = 0.03

#Variables
stock_price = 40.00
stock_purchase_total = stock_price * STOCK_QUANTITY
stock_purchase_commission = stock_purchase_total * STOCK_COMMISSION
stock_price = 42.75
stock_sold_total = stock_price * STOCK_QUANTITY

#Print Results
# The amount of money Joe paid for the stock.
print(f'The amount of money Joe paid for the stock is: ${stock_purchase_total:.2f}')

# The amount of commission Joe paid his broker when he bought the stock.
print(f'The amount of commission Joe paid his broker when he bought the stock is: ${stock_purchase_commission:.2f}')

# The amount of money Joe sold the stock for.
print(f'The amount of money Joe sold the stock for is: ${stock_sold_total:.2f}')
