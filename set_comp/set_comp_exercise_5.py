'''
calculate the probability that in three throws of symmetrical cubic dice, the sum of the squares of points will be divisible by 3
'''

def calc_probability_of_sq_of_3_nums_divisibile_by_3():
    omega = {(i, j, k) 
             for i in range(1, 7) 
             for j in range(1, 7) 
             for k in range(1, 7)}
    squares_div_by_3 = {(x, y, z) for x, y, z in omega if (x**2 + y**2 + z**2) % 3 == 0}
    print(squares_div_by_3)
    probability = len(squares_div_by_3) / len(omega)
    print(round(probability, 4))

calc_probability_of_sq_of_3_nums_divisibile_by_3()