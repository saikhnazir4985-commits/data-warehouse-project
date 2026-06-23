import pandas as pd
from sqlalchemy import create_engine

def start_engine():

    server = r"localhost\SQLEXPRESS01"
    database = "DataWarehouse"

    connection_url = (
        f"mssql+pyodbc://@{server}/{database}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&trusted_connection=yes"
        "&TrustServerCertificate=yes"
    )

    engine = create_engine(connection_url)

    return engine
'''
engine = start_engine()

query = "select count(*) from bronze.crm_cust_info"

df = pd.read_sql(query, engine)

print(df)
'''