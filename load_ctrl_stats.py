import pandas as pd

def load_stats(excel_file):
    df= pd.read_excel(excel_file)
    return df

print(load_stats("qc_1.xlsx"))