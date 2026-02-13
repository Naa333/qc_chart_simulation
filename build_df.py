import pandas as pd

def build_df(data_dict, start_date): #num_of_entries has to be the same
    df = pd.DataFrame(data_dict)
    #add date column. Generate a sequence of dates from the specified date daily, 'D', up to the length of vertical cols
    df['dates']= pd.date_range(
                         start= start_date, 
                         periods= len(df.index), 
                         freq= 'D'
                         ) 
    return df