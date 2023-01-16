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
    return max(odd)

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
    return min(odd)

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
    return max(even)
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
    return min(even)

def oldest_user(users: list[dict]) -> dict:
    '''returns the oldest user in the list 'users' given as an argument. (you may use max, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the oldest user
    '''
    return max(users, lambda user: user['age'])
    print(oldest_user(users))

def youngest_user(users: list[dict]) -> dict:
    '''returns the youngest user in the list 'users' given as an argument. (you may use min, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the youngest user
    '''
    return min(users, lambda user: user['age'])
    print(youngest_user(users))