'''
calculate the years to double investment at a given interest rate
'''

def calculate_length_of_investment(principal: int, interest_rate: float) -> tuple:
    double_amount = principal * 2
    amount = principal
    years = 0
    while amount < double_amount:
        amount += amount * interest_rate
        years += 1

    return (years, amount)

investment_info = calculate_length_of_investment(1000, 0.04)
print(f'Future value: {round(investment_info[1], 2)} USD. Number of years: {investment_info[0]}')

