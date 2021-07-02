def fixedPayment(balance, annualInterestRate):
    """

    Parameters
    ----------
    balance :               The outstanding balance on the credit card
    annualInterestRate :    Annual interest rate as a decimal

    Returns
    -------
    Lowest Payment:         Minimum fixed monthly payment needed in order 
                            pay off a credit card balance within 12 months

    """
    
    month = 1
    while month <= 12:
        balance -= minPay
        balance += (annualInterestRate/12.0)*balance
        month += 1
    if balance <= 0:
        return minPay
    else:
        return False

rerun = True
minPay = 0

while rerun == True:
    if fixedPayment(balance, annualInterestRate) == False:
        minPay += 10
        fixedPayment(balance, annualInterestRate)
    else:   
        print("Lowest Payment: " + str(round(minPay,2)))
        rerun = False
