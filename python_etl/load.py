
def load_table(df, table_name, engine):
    
    try:
        #print(f'Loading into table {table_name}...')

        df.to_sql(
            name = table_name,
            con = engine,
            schema = 'bronze',
            if_exists = 'append',
            index = False
        )
        #print(f'Loading completed for table {table_name}')
        return table_name
    except Exception as e:
        print(f"Error occured while loading into {table_name}")
        raise