import csv

def find_name(dname):
	dname = dname.split('(')
	if (len(dname) > 1):
		dname = dname[0].split(' ')
		dname = ' '.join(dname[0:-1])
	else:
		dname = dname[0]	
	return dname	

def making_float(num):
	num = num.split(',')
	if len(num) > 2 :
		mid = ''.join(num[0:-1])
		num = '.'.join([mid,num[-1]])
	else :
		num = '.'.join(num)	
	num = float(num)
	return num	

def filtered_variables(TableName,description):
	years = 'TimePeriod'
	descs = 'LineDescription'
	values = 'DataValue'
	tdict={years:[], descs:[], values:[]}
	csvFile = csv.reader(open(TableName+'.csv', 'rb'))
	for row in csvFile:
		tdict[years].append(row[8])
		tdict[descs].append(row[2])
		tdict[values].append(row[1])
	Desc_years = []
	Desc_values = []
	for i, desc in enumerate(tdict[descs]):
		if (find_name(desc) == description):
			Desc_years.append(tdict[years][i])
			Desc_values.append(tdict[values][i])
	final_Desc_years = []
	final_Desc_values = []
	for i, year in enumerate(Desc_years):
		if (int(year) > 1990 and int(year) < 2015 ):
			final_Desc_years.append(Desc_years[i])
			final_Desc_values.append(Desc_values[i])
	return final_Desc_values


def Total_GDP():
	values = filtered_variables('T10101', 'Gross domestic product')
	return values

def Housing():
	fur = filtered_variables('T20405', 'Furnishings and durable household equipment')
	hous = filtered_variables('T20405', 'Housing and utilities')
	housM = filtered_variables('T20405', 'Household maintenance')
	housCom = filtered_variables('T31505', 'Housing and community services')
	resid = filtered_variables('T50405', 'Residential')
	# print resid
	total = []
	for i in range(len(fur)):

		total.append(making_float(fur[i])+making_float(hous[i])+making_float(housM[i])+making_float(housCom[i])+making_float(resid[i]))
		
	return total	


def Healthcare():
	thera = filtered_variables('T20405', 'Therapeutic appliances and equipment (42)')
	pharma = filtered_variables('T20405', 'Pharmaceutical and other medical products')
	healthC = filtered_variables('T20405', 'Health care')
	health = filtered_variables('T31505', 'Health')
	med = filtered_variables('T50505', 'Medical equipment and instruments')
	healthC2 = filtered_variables('T20405', 'Health care')
	total = []

	for i in range(len(thera)):

		total.append(making_float(thera[i])+making_float(pharma[i])+making_float(healthC[i])+making_float(health[i])+making_float(med[i])+making_float(healthC2[i]))
		
	return total



def Food():
	food = filtered_variables('T20405', 'Food and beverages purchased for off-premises consumption')
	tob = filtered_variables('T20405', 'Tobacco')
	foods = filtered_variables('T20405', 'Food services')
	agr = filtered_variables('T31505', 'Agriculture')
	foodp = filtered_variables('T40205', 'Foods, feeds, and beverages')
	farmc = filtered_variables('T50405', 'Farm')
	agrm = filtered_variables('T50505', 'Agricultural machinery')
	farm = filtered_variables('T50705A', 'Farm')
	farm1 = filtered_variables('T50705B', 'Farm')
	farm.extend(farm1) 
	total = []

	for i in range(len(food)):

		total.append(making_float(food[i])+making_float(tob[i])+making_float(foods[i])+making_float(agr[i])+making_float(foodp[i])+making_float(farmc[i])+making_float(agrm[i])+making_float(farm[i]))
		
	return total	


def Education():
	edub = filtered_variables('T20405', 'Educational books')
	edus = filtered_variables('T20405', 'Education services')
	edu = filtered_variables('T31505', 'Education')
	eduv = filtered_variables('T50405', 'Educational and vocational')

	total = []

	for i in range(len(edub)):

		total.append(making_float(edub[i])+making_float(edus[i])+making_float(edu[i])+making_float(eduv[i]))
		
	return total

## three dims : search for write column in csv
def create_csv():
	total_Gdp = Total_GDP()
	housing = Housing()
	healthcare = Healthcare()
	food = Food()
	education = Education()
	all_data = [total_Gdp, housing, healthcare, food, education]
	with open("output.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(all_data)

create_csv()
# Housing()