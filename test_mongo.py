from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://moka:aSl9FRN09Vp1qgUSY55ZnWScwScie2nzGrxhiYdGs4ok5ShkGGpJ7zCvU1aKInpLCzgPfJQWNrIEzLC7wp1VHQ==@moka.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")
## assign new db
db = client['test']
## access db
# coll = db['test']
akef = db.test
print coll
