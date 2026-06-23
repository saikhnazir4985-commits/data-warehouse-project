import pandas as pd
from sqlalchemy import text
from connection import start_engine

engine = start_engine()

def truncate_table (table_name):
    #print(f'\nStarting Truncate for Table bronze.{table_name}')
    
    with engine.begin() as conn:
        conn.execute(text(f'Truncate Table bronze.{table_name}'))
    
    #print(f'Truncated Table bronze.{table_name}')
    #print('Validating row count after truncate...')

    query = pd.read_sql(f'select count(*) from bronze.{table_name}', engine)
    #print(f'Row count after truncate: {query}')
    return table_name