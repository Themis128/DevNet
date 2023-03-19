#!/usr/bin/env python3
# Reference:
# https://github.com/meraki/dashboard-api-python/
import meraki
import pprint

api_key='6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
url = 'https://dashboard.meraki.com'
org_name = 'DevNet Sandbox'

dashboard = meraki.DashboardAPI(
    api_key=api_key,
    base_url= url + '/api/v0/',
    output_log=False,
    print_console=False
)

# Step 1. Retrieves an organization's ID from Meraki dashboard API based on organization name
org_list = dashboard.organizations.getOrganizations()
for org in org_list:
    if org['name'] == org_name:
        my_org_id = org['id']

# Step 2. write a function that retrieves organization inventory based on ID
inventory_list = dashboard.organizations.getOrganizationInventory(my_org_id)

# Step 3. print out the inventory list and write it to a file named inventory_list.txt with
# one item per line
pprint.pprint(inventory_list)
with open('inventory_list.txt', 'w') as f:
    for item in inventory_list:
        f.write(str(item))
        f.write('\n')





