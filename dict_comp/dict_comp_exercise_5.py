'''
Create a list consisting of dictionaries mapping consecutive digits from 1 to 9 inclusive 
to their respective k-th powers, for k = 1, 2, 3.
'''

def create_list_of_dicts_showing_nth_powers() -> list:
    list_of_powers = [{i: i**j for i in range(1, 10)} for j in range(1, 4)]
    print(list_of_powers)


create_list_of_dicts_showing_nth_powers()