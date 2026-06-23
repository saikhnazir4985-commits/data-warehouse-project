#part1


from connection import start_engine
import pandas as pd
from sqlalchemy import text
from truncate import truncate_table
from extract import extract_data
from load import load_table
from dashboard import generate_dashboard
'''
file_path = (r"C:\Project_2\data_warehouse_project\datasets\source_crm\cust_info.csv")

#   extracting csv
extr_data = extract_data(file_path)
print(extr_data)

#   engine ready to connect
engine = start_engine()

#   validating table row count
print('validating table row count')
count_val_query = 'SELECT COUNT(*) FROM bronze.crm_cust_info'
print(pd.read_sql(count_val_query, engine))
print()

#   truncate table
truncate_table('crm_cust_info')

#   load
print('starting load')
load_table(extr_data, 'crm_cust_info', engine)

#   validate load
print('validating load')
count_val_query = 'SELECT COUNT(*) FROM bronze.crm_cust_info'
print(pd.read_sql(count_val_query, engine))
'''
'''
datasets = {
        "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\prd_info.csv",
        "table_name":"crm_prd_info"
        }
#print(f'datasets: {datasets}')
for d, t in datasets.items():
    if t == 0:
        print(f't: {t}')
        '''
'''
datasets = [
    {
        "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\cust_info.csv",
        "table_name": "crm_cust_info"
    },
    {
        "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\px_cat_g1v2.csv",
        "table_name":"erp_px_cat_g1v2"
    }
            ]

for d in datasets:
    print(d["table_name"].replace("erp_", "").replace("crm_", ""))
    log(d["table_name"].replace("erp_", "").replace("crm_", ""))

#for d in datasets:
 #   print(d["file_path"])

table_name = "erp_px_cat_g1v2"
#print(table_name.replace('erp_',''))

def add(a,b):
    c = a+b
    return c
add(4,6)
print(add)
log(add)

import logging
import logs

logging.INFO("ncbdyvw")
'''
#part2

from connection import start_engine
# import pandas as pd
# from sqlalchemy import text
# from truncate import truncate_table
# from extract import extract_data
# from load import load_table
# import logging
# import logs

# datasets = [
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\cust_info.csv",
#         "table_name": "crm_cust_info"
#     },
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\prd_info.csv",
#         "table_name":"crm_prd_info"
#     },
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_crm\sales_details.csv",
#         "table_name":"crm_sales_details"
#     },
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_erp\CUST_AZ12.csv",
#         "table_name":"erp_cust_az12"
#     },
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_erp\LOC_A101.csv",
#         "table_name":"erp_loc_a101"
#     },
#     {
#         "file_path":r"C:\Project_2\data_warehouse_project\datasets\source_erp\PX_CAT_G1V2.csv",
#         "table_name":"erp_px_cat_g1v2"
#     }
#             ]

# #   engine ready to connect
# engine = start_engine()

# for d in datasets:
#     file_path = d["file_path"]
#     table_name = d["table_name"]

#     source_table_name = table_name.replace('erp_', '').replace('crm_', '')
#     df = extract_data(file_path)
#     print(f"\nData from {source_table_name}.csv:\n{df.head()}")
    
#     truncate_table(table_name)

#     print('Starting Load...')
#     load_table(df, table_name, engine)

#     query = pd.read_sql(f'select count(*) from bronze.{table_name}', engine)
#     print(f'Row count after load: {query}')

# import logging
# import logs
# from exec_procedure import execute_procedure
# engine = start_engine()
# execute_procedure(engine, "silver.load_silver")

#   engine ready to connect
# engine = start_engine()
# generate_dashboard(engine)

# datasets = [
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\cust_info.csv",
#             "table_name": "crm_cust_info"
#         },
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\prd_info.csv",
#             "table_name": "crm_prd_info"
#         },
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_crm\sales_details.csv",
#             "table_name": "crm_sales_details"
#         },
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\CUST_AZ12.csv",
#             "table_name": "erp_cust_az12"
#         },
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\LOC_A101.csv",
#             "table_name": "erp_loc_a101"
#         },
#         {
#             "file_path": r"C:\Project_2\data_warehouse_project\datasets\source_erp\PX_CAT_G1V2.csv",
#             "table_name": "erp_px_cat_g1v2"
#         }
#     ]
# for d in datasets:
#     # print(f"datasets: {d}")
#     table_name = d["table_name"]
#     print(f"table_name: {table_name}")

