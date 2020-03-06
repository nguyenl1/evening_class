"""
Dictionaries 

Key-values pairs

dict literals (bracket to bracket)
{'key': 'value' } 
[ array: list of strings ]

Immutable value (int, float, string, tuple)
List and dicts cannot be keys

"""

product_to_price = {'apple': 1.0, "pear": 1.5, "grapes": 0.75}
print(product_to_price['apple'])

# print(product_to_price[1.0]) #can only access a dictionary through key not value. 


#update dictionary

product_to_price['apple'] = 300 

print(product_to_price['apple'])

# add to the dictionary

product_to_price['avocado'] = 5000

print(product_to_price['avocado'])

#checking if key exist

if 'apple' in product_to_price:
    print('apple ' + str(product_to_price['apple'])) 

#merge dictionaries

product_to_price.update({'banana': 0.25})
print(product_to_price)

#list of all the keys, values, and items

print(list(product_to_price.keys()))
print(list(product_to_price.values()))
print(list(product_to_price.items()))

#order dict 

print(sorted(product_to_price.keys()))

names_and_colors = [('alice', "red"), ('david', 'green')]
new_dict = dict(names_and_colors)
print(new_dict)


