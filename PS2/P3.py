low  = balance / 12 
high = (balance * (1 + (annualInterestRate/12.0))**12.0) / 12.0
minPay = (low + high) / 2
rerun = True

#low is the lowest minimum possible payment, i.e., when interest is 0%
#high is highets possible payment, i.e., when one payment made at the end of the year

def FixedPayBis(balance, annualInterestRate, minPay):
    """

    Parameters
    ----------
    balance : The outstanding balance on the credit card
    annualInterestRate : Annual interest rate as a decimal
    minPay : Smallest Monthly payment to the cent

    Returns
    -------
    balance : New outstanding balance on the credit card

    """
    month = 1
    while month <= 12:
        balance -= minPay
        balance += balance*(annualInterestRate/12.0)
        month += 1
    return balance

while rerun == True:
    a = FixedPayBis(balance, annualInterestRate, minPay)
    if round(a) < 0:
        high = minPay
        minPay = (low + high) / 2
    elif round(a) > 0:
        low = minPay
        minPay = (low + high) / 2
    elif round(a) == 0:
        rerun = False
        print("Lowest Payment: " + str(round(minPay,2)))
