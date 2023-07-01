'''
Depending on the interest rates given below, 
calculate the value of interest on investments:
'''

def calc_future_investment_value(pv=1000, n=10) -> list:
    rates =  [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
    interest = [round(pv * (1 + rate)**n  - pv, 2) for rate in rates]
    print(interest)

calc_future_investment_value(1000, 10)