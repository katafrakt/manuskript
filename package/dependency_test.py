import os
import sys

realpath = os.path.realpath(__file__)

sys.path.insert(1, os.path.join(os.path.dirname(realpath), '..'))

from manuskript import main

# import enchant;
# print(enchant.list_dicts())
# default = enchant.get_default_language('en_US')
# print(default)
# enchant.Dict(default)
