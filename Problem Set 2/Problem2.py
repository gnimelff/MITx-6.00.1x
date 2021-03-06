# Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
# 
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# 
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.
# 
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months.


monthlyinterest = annualInterestRate / 12
test = (balance // 12) - (balance // 12 % 10)   #sets initial payment test to nearest factor of 10 of balance / 12
original_balance = balance

while True:
    for months in range(1, 13):
        balance -= test
        balance += (balance * monthlyinterest)
    if balance <= 0:
        break
    else:
        balance = original_balance
        test += 10

print('Lowest payment: ' + str(test))
