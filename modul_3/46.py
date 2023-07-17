"""
Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, or {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
"""
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combine = {}

for i in item_list:
    key = i ['item']
    value = i ['amount']

    if key not in combine:
        combine[key] = value
    else :
        combine[key] += value

print(combine)