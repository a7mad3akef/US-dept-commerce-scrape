from urllib import urlopen
import json
from config import frequency_parameters, DatasetName, Years, TableName, key
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
client = MongoClient("mongodb://moka:aSl9FRN09Vp1qgUSY55ZnWScwScie2nzGrxhiYdGs4ok5ShkGGpJ7zCvU1aKInpLCzgPfJQWNrIEzLC7wp1VHQ==@moka.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")
## assign new db
db = client['tables']

tables = []

def push_table_data(table_data,TableName):
	vart = []
	
	for i in range(len(table_data)):
		
		if(i % 200 == 0):
			vart.append(table_data[i])
			# print vart
			result = db[TableName].insert_many(vart)
			vart = []
			print '-----------------------------------------------------------------------------'	 
		elif( i == len(table_data)-1):
			vart.append(table_data[i])
			# print vart
			result = db[TableName].insert_many(vart)
			vart = []
			print '-----------------------------------------------------------------------------'	
			print('the last is '+str(i))
		else:
			vart.append(table_data[i])
			print str(i) + ' from '+ str(len(table_data))

		# result = db.table.insert_many(table_data)
	print 'finished'	



def get_dataset_tables(DatasetName):
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetParameterValues&ParameterName=TableName&datasetname='+DatasetName+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['ParamValue']
	for table in data:
		tables.append(table['TableName'])

# get_dataset_tables(DatasetName)
# print tables

def get_table_data(TableName):
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName+'&Frequency='+frequency_parameters+'&Year=X&ResultFormat=JSON'
	sauce = urlopen(link).read().split('<!DOCTYPE')[0]
	parsed = json.loads(sauce)['BEAAPI']['Results']['Data']
	print 'writing now'
	# result = db.restaurants.insert_one(parsed)
	# print result.inserted_id

	# with open(TableName+'.csv','w') as file:
	# 	file.write(json.dumps(parsed, indent=4, sort_keys=True))
	push_table_data(parsed,TableName)
	
# get_table_data(TableName)	

def get_table_data_year(TableName, Year):
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName+'&Frequency='+frequency_parameters+'&Year='+Year+'&ResultFormat=JSON'
	sauce = urlopen(link).read().split('<!DOCTYPE')[0]
	parsed = json.loads(sauce)['BEAAPI']
	return json.dumps(parsed, indent=4, sort_keys=True)


def get_all_data():
	aDict = {}
	i = 1
	get_dataset_tables(DatasetName)
	print 'finished tables'
	for table in tables:
		aDict[table] = get_table_data_year(table,'2015')
		i = i+1
		print str(i) +' from '+ str(len(tables)) 
	print 'writing now'
	with open('all.csv','w') as file:
		file.write(json.dumps(aDict, indent=4, sort_keys=True))	


def load_table_data(TableName):
	result = dumps(db[TableName].find(), indent=4, sort_keys=True)
	# print result
	# for document in result:
	# 	print(document)
	# dumps(c.test.test.find())
	with open(TableName+'.csv','w') as file:
		file.write(result)

# get_table_data('T50505')
load_table_data('T50505')

