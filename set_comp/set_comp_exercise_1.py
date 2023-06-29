'''
probability space for getting a sum of points higher than 10
'''

def probability_space():
    omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
    sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
    return len(sum_gt_10) / len(omega)

print(probability_space())