# create a lambda function that returns the first element of the list 'l' given as an argument, then assign it to variable 'first1'.
first1 = lambda l: l[0]
print(first1([1, 2, 3, 4]))
# create a lambda function that returns the last element of the list 'l' given as an argument, then assign it to variable 'last1'.
last1 = lambda l: l[-1]
print(last1([1, 2, 3, 4]))
# create a lambda function that returns the length of the list 'l' given as an argument, then assign it to variable 'length1'.
length1 = lambda l: len(l)
print(length1([a,b, c, d, e, f]))
# create a lambda function that returns the first element of the tuple 't' given as an argument, then assign it to variable 'first2'.
first2 = lambda t: t[0]
print(first2((1, 2, 3, 4)))
# create a lambda function that returns the last element of the tuple 't' given as an argument, then assign it to variable 'last2'.
last2 = lambda t: t[-1]
print(last2((a, b, c, d, e, f)))
# create a lambda function that returns the length of the tuple 't' given as an argument, then assign it to variable 'length2'.
length2 = lambda t: len(t)
print(length2((a, b, c, d, e, f)))
# create a lambda function that returns the value in key 'age' of the dict 'd' given as an argument, then assign it to variable 'age'.
age = lambda d: d["age"]
print(age({('age': 21), ('name': "Farrukh"), ('surname': "Ravshanov")}))
# create a lambda function that returns the value in key 'name' of the dict 'd' given as an argument, then assign it to variable 'name'.
name = lambda d: d["name"]
print(age({('age': 21), ('name': "Farrukh"), ('surname': "Ravshanov")}))