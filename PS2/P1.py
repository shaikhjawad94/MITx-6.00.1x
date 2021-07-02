totpaid = 0
month = 1
while month <= 12:
    minPay = balance * monthlyPaymentRate
    balance -= minPay
    balance += balance * (annualInterestRate/12.0)
    totpaid += minPay
    month += 1
print('Remaining Balance: ' + str(round(balance,2)))
