#!/usr/bin/env python3
#
# Sort the inventory file 'inventory_list.txt' by model and device count,
# return the result in a Python dictionary
#
# Example line:
# {'mac': 'e0:cb:bc:8c:c2:4a', 'serial': 'Q2KD-5BTF-CA87',
#  'networkId': None, 'model': 'MR42', 'claimedAt': '1552300296.10688',
#  'publicIp': None, 'name': ''}
#
from pprint import pprint
from ast import literal_eval


# Step 1. Read from file and put each models in a list
def inventory_model_list(filename):
    models = []
    with open(filename, 'r') as f:
        for item in f.readlines():
            item_dict = literal_eval(item)
            models.append(item_dict['model'])
        return models


# Step 2. Get the count of each model
def model_count(model_list):
    unique_items = []
    for item in model_list:
        if item not in unique_items:
            unique_items.append(item)
    model_count_dict = {}
    for i in unique_items:
        model_count_dict[i] = model_list.count(i)
    return model_count_dict


if __name__ == "__main__":
    filename = 'inventory_list.txt'
    model_list = inventory_model_list(filename)
    final_count_list = model_count(model_list)
    pprint(final_count_list)

 'w') as f:
    for item in inventory_list:
        f.write(str(item))
        f.write('\n')

6.57', 'name': ''}
{'mac': '88:15:44:60:21:10', 'serial': 'Q2MD-BHHS-5FDL', 'networkId': 'L_646829496481105433', 'model': 'MR53', 'claimedAt': '1495638330.96262', 'publicIp': '64.103.26.57', 'name': ''}
{'ma