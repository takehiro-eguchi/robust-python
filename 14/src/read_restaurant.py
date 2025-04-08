import yaml
from pprint import pprint

with open("restaurant.yaml") as yaml_file:
    restaurant = yaml.safe_load(yaml_file)
    pprint(f'yaml = {restaurant}')
