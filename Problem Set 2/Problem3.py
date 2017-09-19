# Write a program that uses bisection search to find the smallest monthly payment to the cent such that we can pay off the debt within a year.
# The following variables are given:
#     balance - the outstanding balance on the credit card
#     annualInterestRate - annual interest rate as a decimal

monthlyinterest = annualInterestRate / 12
orig_bal = balance
low = balance / 12
high = (balance * (1 + monthlyinterest)**12) / 12.0

while abs(balance) > 0.01:
    test = (low + high) / 2
    balance = orig_bal
    
    for months in range(12):
        balance -= test
        balance += (balance * monthlyinterest)
        
    if balance > 0.01:
        low = test
    elif balance < 0.01:
        high = test
        
print('Lowest payment: ' + str(round(test, 2)))
