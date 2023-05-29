'''
read file and find the highestvolume for the month
'''

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [line.split(',')[-1] for line in content][1:]
max_volume = ma

print(volumes)
