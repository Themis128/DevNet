#!/usr/bin/env python
# pip install pyyaml
import yaml
from pprint import pprint as pp

document = """
---
a: 1
b: 
  c: 3
  d: 4
  e: 
    - aa
    - bb
    - cc
"""

# from YAML obj to Python
# https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
yaml_to_python = yaml.load(document, Loader=yaml.FullLoader)
pp(type(yaml_to_python))
pp(yaml_to_python)

# decode Python to YAML
python_to_yaml = yaml.dump(yaml_to_python)
pp(python_to_yaml)

# decode YAML to Python object
with open('Ansible_Network_Facts_Demo.yml', 'r') as f:
    ansible_playbook = yaml.load(f.read())

# interpret result
pp(type(ansible_playbook))
pp(ansible_playbook)
