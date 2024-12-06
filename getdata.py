## pupose of this file: reading the data, converting it into mongo format and then pushing the data

import os
import sys
import json

from dotenv import load_dotenv 
load_dotenv()

MONGO_DB_URL = os.getenv('MONGODB_URL')
print(MONGO_DB_URL)

## Certifi will help to get the SSL based connection
import certifi
ca = certifi.where() 

import pandas as pd
import numpy as np