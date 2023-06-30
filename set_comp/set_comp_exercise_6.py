'''
We roll the symmetrical dice three times. Calculate the probability of the following:

 - odd number of points in each roll
'''

def calc_probability_odd_num_of_3_rolls():
    omega = {(i, j, k) 
             for i in range(1, 7) 
             for j in range(1, 7) 
             for k in range(1, 7)}
    
    odd_num_for_3 = {(x, y, z) for x, y, z in omega if x % 2 != 0 and y % 2 != 0 and z % 2 != 0}
    print(odd_num_for_3)
    probability = len(odd_num_for_3) / len(omega)
    print(probability)

calc_probability_odd_num_of_3_rolls()