'''
find the day with the highest volume
'''

with open('playway.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
volumes = [(volume[0], int(volume[1])) for volume in volumes]
max_volume = max([val[1] for val in volumes])
max_date = list(filter(lambda val: val[1] == max_volume, volumes))[0][0]
# print(max_volume)
print(max_date)
# print(volumes)