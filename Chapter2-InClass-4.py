priceOne = float(input("Enter the price of item 1: "))
priceTwo = float(input("Enter the price of item 2: "))
priceThree = float(input("Enter the price of item 3: "))
priceFour = float(input("Enter the price of item 4: "))
priceFive = float(input("Enter the price of item 5: "))

salesTax = 0.07

priceSubTotal = priceOne + priceTwo + priceThree + priceFour + priceFive
priceTotal = priceSubTotal * (1 + salesTax)

print("The subtotal is $", priceSubTotal)
print("The total is $", priceTotal)
