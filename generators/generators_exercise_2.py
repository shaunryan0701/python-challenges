'''
a generator enumerator
'''

def enum(input_list: list) -> iter:
  count = 0
  for item in input_list:
    yield (count, item)
    count += 1

print(list(enum(['TEN', 'CDR', 'BBT'])))