## import dependencies
from urllib import urlopen
import json
from config import frequency_parameters, DatasetName, Years, TableName, key
from pymongo import MongoClient
from bson.json_util import dumps

## create db connection
client = MongoClient()
client = MongoClient("mongodb://moka:aSl9FRN09Vp1qgUSY55ZnWScwScie2nzGrxhiYdGs4ok5ShkGGpJ7zCvU1aKInpLCzgPfJQWNrIEzLC7wp1VHQ==@moka.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")

## assign new db
db = client['tables']

tables = []

## to push chunks of a table data to Azure
def push_table_data(table_data,TableName):
	vart = []
	
	for i in range(len(table_data)):
		
		if(i % 200 == 0):
			vart.append(table_data[i])
			
			result = db[TableName].insert_many(vart)
			vart = []
			print '----------------------------------table: '+TableName+'-------------------------------------------'	 
		elif( i == len(table_data)-1):
			vart.append(table_data[i])

			result = db[TableName].insert_many(vart)
			vart = []
			print '-----------------------------------table: '+TableName+'------------------------------------------'	
			print('the last is '+str(i))
		else:
			vart.append(table_data[i])
			print str(i) + ' from '+ str(len(table_data)) +' in table '+ TableName

		
	print 'finished pushing '+ TableName	


## to get the data of a table
def get_table_data(TableName):
	
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName+'&Frequency='+frequency_parameters+'&Year=X&ResultFormat=JSON'
	
	try:
		sauce = urlopen(link).read().split('<!DOCTYPE')[0]

		parsed = json.loads(sauce)['BEAAPI']['Results']['Data']
	
		print 'writing now'
		
		push_table_data(parsed,TableName)

	except:
	    
	    print 'The table : '+TableName+' hasn\'t any data for any frequency!'
	
	
	




## to get all the tables 
def get_dataset_tables(DatasetName):
	
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetParameterValues&ParameterName=TableName&datasetname='+DatasetName+'&ResultFormat=JSON'
	
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['ParamValue']
	
	for table in data:
		tables.append(table['TableName'])

def get_all_data(DatasetName):
	
	get_dataset_tables(DatasetName)
	# print tables
	for table in tables:
		get_table_data(table)
	

get_all_data(DatasetName)
# get_table_data('T50705B')