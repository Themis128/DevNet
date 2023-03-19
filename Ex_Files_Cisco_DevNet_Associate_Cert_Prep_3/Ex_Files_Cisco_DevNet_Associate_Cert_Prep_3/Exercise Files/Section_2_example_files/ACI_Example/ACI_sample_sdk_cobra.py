#/usr/bin/env python3
# Reference from:
# https://github.com/CiscoDevNet/aci-learning-labs-code-samples/blob/master/sbx-intermediate-aci/sbx-intermediate-aci-02_cobra/cobra_tenant.py
# https://developer.cisco.com/learning/modules/intermediate-aci-prog/sbx-intermediate-aci-02_cobra/step/1
# 
# To disable urllib3 warning: 
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"
# Installation https://cobra.readthedocs.io/en/latest/install.html#installation-requirements
from credentials import *
import cobra.mit.session
import cobra.mit.access
import cobra.mit.request

auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
session.login()

tenant_query = cobra.mit.request.DnQuery("uni/tn-Heroes")
heroes_tenant = session.query(tenant_query)
heroes = heroes_tenant[0]
print(heroes.name)
print(heroes.dn)
