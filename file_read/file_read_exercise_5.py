'''
find the day with the highest volume
'''

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
volumes = [(volume[0], int(volume[1])) for volume in volumes]
print(volumes)