## import dependencies
from urllib import urlopen
import json
from config import frequency_parameters, DatasetName, key, tables
from pymongo import MongoClient
from bson.json_util import dumps
import csv

client = MongoClient()
client = MongoClient("mongodb://moka:aSl9FRN09Vp1qgUSY55ZnWScwScie2nzGrxhiYdGs4ok5ShkGGpJ7zCvU1aKInpLCzgPfJQWNrIEzLC7wp1VHQ==@moka.documents.azure.com:10255/?ssl=true&replicaSet=globaldb")
## assign new db
db = client['tables']


## to get table data from the BEA api
def get_table_data(TableName):
	
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName+'&Frequency='+frequency_parameters+'&Year=X&ResultFormat=JSON'
	
	sauce = urlopen(link).read().split('<!DOCTYPE')[0]
	
	parsed = json.loads(sauce)['BEAAPI']['Results']['Data']
	
	print 'writing now'
	
	push_table_data(parsed,TableName)

## to get the data from the db
def load_table_data(TableName):
	
	print 'loading table: '+ TableName

	result = dumps(db[TableName].find())

	x = json.loads(result)

	print 'writing table: '+ TableName

	f = csv.writer(open(TableName+'.csv', 'wb+'))

	f.writerow(['CL_UNIT', 'DataValue', 'LineDescription', 'LineNumber', 'METRIC_NAME','SeriesCode', 'TableID', 'TableName', 'TimePeriod', 'UNIT_MULT', '_id'])

	for x in x:
		f.writerow([x['CL_UNIT'],
					x['DataValue'],
					x['LineDescription'],
					x['LineNumber'],
					x['METRIC_NAME'],
					x['SeriesCode'],
					x['TableID'],
					x['TableName'],
					x['TimePeriod'],
					x['UNIT_MULT'],
					x['_id']['$oid']])


def load_tables_data(tables):
	
	for table in tables:
	
		load_table_data(table)


load_tables_data(tables)


