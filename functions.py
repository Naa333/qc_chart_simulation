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

def get_std(df, column_name):
    return df[column_name].std()

def get_mean(df, column_name):
    return df[column_name].mean()

def build_df(data_dict, start_date): #num_of_entries has to be the same
    df = pd.DataFrame(data_dict)
    #add date column. Generate a sequence of dates from the specified date daily, 'D', up to the length of vertical cols
    df['dates']= pd.date_range(start= start_date, periods= len(df.index), freq= 'D') 
    return df

def plot_graph(df):
    fig = go.Figure()

    # Add all traces, initially set visible=False except first
    traces = []
    for i, column in enumerate(df.columns[:-1]):  # exclude dates
        visible = (i == 0)  # first one visible
        trace = go.Scatter(
            x=df['dates'],
            y=df[column],
            name=column,
            visible=visible
        )
        fig.add_trace(trace)
        traces.append(column)

        #statistics trace list
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [(get_mean(df, column))]*len(df[column]),
                name= 'Mean',
                visible= (i == 0),
                line= dict(color= "green")

            )
        )
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)-get_std(df, column)]*len(df[column]),
                name= 'Minus One Std Dev',
                visible= (i == 0),
                line= dict(color= "yellow")

            )
        )
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)- (2*get_std(df, column))]*len(df[column]),
                name= 'Minus Two Std Dev',
                visible= (i == 0),
                line= dict(color= "red")

            )
        )
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)+get_std(df, column)]*len(df[column]),
                name= 'Plus One Std Dev',
                visible= (i == 0),
                line= dict(color= "yellow")
            )
        )
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)+ (2*get_std(df, column))]*len(df[column]),
                name= 'Plus Two Std Dev',
                visible= (i == 0),
                line= dict(color= "red")
            )
        )
    
    return fig