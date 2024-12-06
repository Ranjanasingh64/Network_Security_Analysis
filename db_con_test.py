
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://power:shakti123@mlcluster.7moqz.mongodb.net/?retryWrites=true&w=majority&appName=MLCluster"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)