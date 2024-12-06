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
import pymongo




from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

## the below class is responsible to read your data from local file and do the conversion from table to json and finally push it to MONGO

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def csv_to_json_converter(self, file_path):
            try:
                data = pd.read_csv(file_path)
                data.reset_index(drop=True, inplace=True)
                records = list(json.loads(data.T.to_json()).values())
                return records
            
            except Exception as e:
                raise NetworkSecurityException(e, sys)   
        
        
    def pushing_data_to_mongo(self, records, database, collection):
            try:
                self.database = database
                self.collection = collection
                self.records = records

                self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
                self.database = self.mongo_client[self.database]
                self.collection = self.database[self.collection]
                self.collection.insert_many(self.records)

                return len(self.records)
            
            except Exception as e:
                raise NetworkSecurityException(e,sys)    
            

if __name__ == '__main__':
    FILE_PATH = r"C:\iNeuron_Courses\ineuron_FSDS\Paul_ML_Project\Network_Security_Analysis\network_data\NetworkData.csv"
    DATABASE = 'MLCluster'         
    COLLECTION ='NetworkData'
 
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(FILE_PATH)
    noofrecords = networkobj.pushing_data_to_mongo(records, DATABASE, COLLECTION)
    print(noofrecords)

            
                

