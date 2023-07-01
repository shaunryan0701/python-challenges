'''
Depending on the interest rates given below, 
calculate the future value fv of your investment:
'''

def calc_future_investment_value(pv=1000, n=10) -> list:
    rates =  [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    fv = [round(pv * (1 + rate)**n, 2) for rate in rates]
    print(fv)

calc_future_investment_value(1000, 10)