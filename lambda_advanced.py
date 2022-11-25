import json

data = open('data.json').read()
users = json.loads(data)


def max_odd(l: list) -> int:
    '''returns the maximum odd number in the list 'l' given as an argument. (you may use max, labmda)
    
    Args:
        l (list): list of numbers
        
    Returns:
        int: maximum odd number
    '''
    odd = []
    for i in l:
        if i % 2 == 1:
            odd.append(i)
    lambda l: max(odd)

print(max_odd(users))

def min_odd(l: list) -> int:
    '''returns the minimum odd number in the list 'l' given as an argument. (you may use min, labmda)
    
    Args:
        l (list): list of numbers
        
    Returns:
        int: maximum odd number
    '''
    odd = []
    for i in l:
        if i % 2 == 1:
            odd.append(i)
    lambda l: min(odd)

def max_even(l: list) -> int:
    '''returns the maximum even number in the list 'l' given as an argument. (you may use max, labmda)
    
    Args:
        l (list): list of numbers
        
    Returns:
        int: maximum even number
    '''
    even = []
    for s in l:
        if s % 2 == 0:
            even.append(s)
    
    lambda l: max(even)
def min_even(l: list) -> int:
    '''returns the minimum even number in the list 'l' given as an argument. (you may use min, labmda)
    
    Args:
        l (list): list of numbers
        
    Returns:
        int: maximum even number
    '''
    even = []
    for s in l:
        if s % 2 == 0:
            even.append(s)
    
    lambda l: min(even)

def oldest_user(users: list[dict]) -> dict:
    '''returns the oldest user in the list 'users' given as an argument. (you may use max, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the oldest user
    '''
    ages = []
    for age in l["users"]["age"]:
        if age[0] < age:
            old = age
    return old

def youngest_user(users: list[dict]) -> dict:
    '''returns the youngest user in the list 'users' given as an argument. (you may use min, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the youngest user
    '''
    ages = []
    for age in l["users"]["age"]:
        if age[0] > age:
            young = age
    return young