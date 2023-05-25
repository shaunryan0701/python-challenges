'''
read file and find the highestvolume for the month
'''

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]
max_volume = max(volumes)

print(max_volume)
