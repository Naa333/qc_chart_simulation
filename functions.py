#generating functions for plotting graphs
#create a dummy df of values I can plot
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def generate_data(column_name, data_range, num_of_entries):
    #loop and generate data for each column name (dict)
    #if data type of data range = int, use int random generator
    #else use float
    data= {}
    if isinstance(data_range[0], int):
        rng = np.random.default_rng(42)
        data[column_name]= rng.integers(low= data_range[0], high= data_range[-1], size= num_of_entries)
    else:
        rng = np.random.default_rng(42)
        data[column_name]= np.round(rng.uniform(low= data_range[0], high= data_range[-1], size= num_of_entries), 1)
    return data

def build_df(data_dict, start_date): #num_of_entries has to be the same
    df = pd.DataFrame(data_dict)

    #add date column. Generate a sequence of dates from the specified date daily, 'D', up to the length of vertical cols
    df['dates']= pd.date_range(start= start_date, periods= len(df.index), freq= 'D') 
    return df

def generate_statistics(df):
    return df.std()

def plot_graph(df):
    fig = go.Figure()
    for column in range(len(df.columns)-1):
        fig.add_trace(go.Scatter
                        (x=df['dates'],
                         y=df.iloc[:,column],
                         name=df.columns[column])
                    )
    return fig

# df= build_df({'f': [2,3,4,5], 'y':[4.5, 2.3, 4.2,1.5]}, start_date= 2/4/25)
# for column in range(len(df.columns)-1):
#     print(df.columns[column])