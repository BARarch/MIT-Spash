def balanceYear(balanceNet, monthlyPayment, interest):
    for month in range(12):
        balanceNet = balanceNet - monthlyPayment
        #print(monthlyPayment)
        balanceNet = balanceNet + interest * balanceNet / 12.0 
    return balanceNet

def lowestPaymentIter(low, high, balance, interest):
    if balanceYear(balance, (high + low) / 2, interest) > .001:
        ## Mid Payment too Low, Value is between Mid and High
        print("High: " + str((high + low) / 2))
        return lowestPaymentIter((high + low) / 2, high, balance, interest)
    elif balanceYear(balance, (high + low) / 2, interest) < -.001:
        ## Mid Payment too High, Value is between Low and Mid
        print("Low: "+ str((high + low) / 2))
        return lowestPaymentIter(low, (high + low) / 2, balance, interest)

    else:
        return (high + low) / 2

def lowestPaymentIter2(low, high, balance, interest):
    if round(high, 2) == round(low, 2):
        return round(high,2)
    elif balanceYear(balance, (high + low) / 2, interest) > 0:
        ## Mid Payment too Low, Value is between Mid and High
        ##print("Low: " + str((high + low) / 2))
        return lowestPaymentIter2((high + low) / 2, high, balance, interest)
    else:
        ## Mid Payment too High, Value is between Low and Mid
        ##print("High: "+ str((high + low) / 2))
        return lowestPaymentIter2(low, (high + low) / 2, balance, interest)
    

def lowestPayment(balance, interest):
    monthlyInterest = interest / 12
    low0 = balance / 12
    high0 = (balance * (1 + monthlyInterest)**12) / 12
    return lowestPaymentIter2(low0, high0, balance,interest)

balance = 999999
annualInterestRate = .18
print("Lowest Payment: " + str(lowestPayment(balance, annualInterestRate)))   