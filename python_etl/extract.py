import pandas as pd

def extract_data(file_path):
    
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error occured while extracting from {file_path}")
        raise