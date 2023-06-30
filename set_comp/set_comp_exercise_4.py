'''
calculate the probability of obtaining three values which the sum is divisible by 7
'''

def calc_probability_of_sum_of_3_nums_divisibile_by_7():
    omega = {(i, j, k) 
             for i in range(1, 7) 
             for j in range(1, 7) 
             for k in range(1, 7)}
    div_by_7 = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}
    probability = len(div_by_7) / len(omega)
    print(round(probability, 2))

calc_probability_of_sum_of_3_nums_divisibile_by_7()