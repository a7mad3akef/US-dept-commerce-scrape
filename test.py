import pybea
import json
USER_ID = '98A0A0A7-21DF-4B75-96DE-1410D47AB280'
# # access the BEA data API...
# meta_data = pybea.get_data_set_list(USER_ID)

# # ...display the resulting Pandas DataFrame
# print(meta_data)
# # access the BEA data API...
# meta_data = pybea.get_parameter_list(USER_ID, DataSetName='NIPA')

# # ...display the resulting Pandas DataFrame
# print(meta_data)

# # access the BEA data API...
# meta_data = pybea.get_parameter_values(USER_ID, DataSetName='NIPA',
#                                        ParameterName='KeyCode')

# # ...display the resulting Pandas DataFrame
# print(meta_data)
# access the BEA data API...
# meta_data = pybea.get_parameter_values(USER_ID,
#                                        DataSetName='NIPA',
#                                        ParameterName='Year')

# # ...display the resulting Pandas DataFrame
# out = meta_data.to_json(orient='records')[1:-1].replace('},{', '} {')
parsed = json.loads(out)
print json.dumps(out, indent=4, sort_keys=True)