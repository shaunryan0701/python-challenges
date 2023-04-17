def calculate_compound_interest(capital: int, percentage_rate: float, term_in_years: int=2) -> float:
    amount_at_term = capital * (1 + (percentage_rate/100)) ** term_in_years
    return round(amount_at_term, 2)
    