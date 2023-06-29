'''
calculate probability space of getting square greater than 45
'''

def calculate_prob_of_sums():
    omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
    sq_gt_45 = {(x, y) for x, y in omega if (x**2 + y**2) >= 45}
    print(round(len(sq_gt_45) / len(omega), 2))

calculate_prob_of_sums()