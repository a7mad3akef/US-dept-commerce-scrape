# import dependencies
import bs4 as bs
from urllib import urlopen
import json
from config import frequency_parameters, DatasetName, Years, TableName, key
# declare variables



# if (len(TableName) > 1 ):
# 	for i in range(len(TableName)):
# 		link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName[i]+'&Frequency='+frequency_parameters+'&Year='+Year+'&ResultFormat=JSON'
# 		sauce = urlopen(link).read()

# 		parsed = json.loads(sauce)

# 		data = parsed['BEAAPI']['Results']['Data']
# 		print json.dumps(data, indent=4, sort_keys=True)
# 		print'========================================================================================='+str(i)	
# else:	
# 	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName[0]+'&Frequency='+frequency_parameters+'&Year='+Year+'&ResultFormat=JSON'
# 	sauce = urlopen(link).read()

# 	parsed = json.loads(sauce)
# 	data = parsed['BEAAPI']['Results']['Data']
# 	print json.dumps(data, indent=4, sort_keys=True)



# link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&Frequency='+frequency_parameters+'&Year=X&ResultFormat=JSON'
# link2 = 'https://www.bea.gov/api/data?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetParameterValues&datasetname=NIPA&ParameterName=Year&'
# sauce = urlopen(link2).read()
# parsed = json.loads(sauce)
# print json.dumps(parsed, indent=4, sort_keys=True)
# link2 = '/api/data?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetParameterValues&datasetname=NIPA&ParameterName=Year&'


def p1_1():
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName=T10105&Frequency='+frequency_parameters+'&Year=X&ResultFormat=JSON'
	sauce = urlopen(link).read().split('<!DOCTYPE')[0]
	parsed = json.loads(sauce)
	print 'writing now'
	with open('T10105.csv','w') as file:
		file.write(json.dumps(parsed, indent=4, sort_keys=True))
	# for i in range(len(stimes)):
	# 	track = tracks[i+1]
	# 	file.write(str(stimes[i].text)+','+str(filter_track(track))+','+str(filter_artist(artists[i+1])))
	# 	file.write('\n')

	# print sauce
	parsed = json.loads(sauce)

	# data = parsed['BEAAPI']['Results']['Data']
	# print json.dumps(data, indent=4, sort_keys=True)

def p1_2():
	link = 'https://www.bea.gov/api/data?&UserID='+key+'&method=GetParameterValues&datasetname=NIPA&ParameterName=Year&'	
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['ParamValue']
	print json.dumps(data, indent=4, sort_keys=True)

def get_all_year(dataSet):
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetParameterValues&ParameterName=Year&datasetname='+dataSet+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed
	print json.dumps(data, indent=4, sort_keys=True)
	## idea : get the smallest FirstAnnualYear then count till our year

def get_dataset_data():
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetData&datasetname=NIPA&Frequency='+frequency_parameters+'&Year=X'
	sauce = urlopen(link).read()
	parsed = json.loads(sauce)

	data = parsed
	print json.dumps(data, indent=4, sort_keys=True)

# def p1_3():
# 	# get_all_year('REGIONALINCOME')

def get_all_data(dataSet):
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=GetData&DataSetName='+DatasetName+'&TableName='+TableName[i]+'&Frequency='+frequency_parameters+'&Year='+Year+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['Data']
	print json.dumps(data, indent=4, sort_keys=True)


def get_dataset_params():
	link = 'https://www.bea.gov/api/data/?&UserID=3B5CE6B0-FAF4-4AA8-BF18-C7A051958387&method=getparameterlist&DataSetName='+DatasetName+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed
	print json.dumps(data, indent=4, sort_keys=True)


def get_dataset_tables():
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetParameterValues&ParameterName=TableName&datasetname='+DatasetName+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['ParamValue']
	for table in data:
		print table['TableID']
	# print json.dumps(data, indent=4, sort_keys=True)

def get_dataset_table_data():
	link = 'https://www.bea.gov/api/data/?&UserID='+key+'&method=GetParameterValues&ParameterName=TableName&datasetname='+DatasetName+'&ResultFormat=JSON'
	sauce = urlopen(link).read()

	parsed = json.loads(sauce)

	data = parsed['BEAAPI']['Results']['ParamValue']
	for table in data:
		print table['TableID']
	print json.dumps(data, indent=4, sort_keys=True)


# p1_1()



