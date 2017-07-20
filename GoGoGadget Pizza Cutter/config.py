# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import csv
from SETTINGS import CONFIG_PATH

class atdict(dict):
	__getattr__= dict.__getitem__
	__setattr__= dict.__setitem__
	__delattr__= dict.__delitem__

    
with open(CONFIG_PATH) as f:
    config = atdict(filter(None, csv.reader(f)))
