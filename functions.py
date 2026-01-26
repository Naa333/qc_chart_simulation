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

    data_traces = []
    stats_traces_indices = [] 
    
    for i, column in enumerate(df.columns[:-1]):  # exclude dates
        visible = (i == 0)  # first one visible
        trace = go.Scatter(
            x=df['dates'],
            y=df[column],
            name=column,
            visible=visible
        )
        fig.add_trace(trace)
        data_traces.append(column)

    # Add statistics traces and track their indices
    for column in df.columns[:-1]:
        i = df.columns.get_loc(column)
        stats_indices = []  # Store trace indices for this parameter's stats
        
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [(get_mean(df, column))]*len(df[column]),
                name= 'Mean',
                visible= (i == 0),
                line= dict(color= "green")
            )
        )
        stats_indices.append(len(fig.data) - 1)
        
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)-get_std(df, column)]*len(df[column]),
                name= 'Minus One Std Dev',
                visible= (i == 0),
                line= dict(color= "yellow")
            )
        )
        stats_indices.append(len(fig.data) - 1)
        
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)- (2*get_std(df, column))]*len(df[column]),
                name= 'Minus Two Std Dev',
                visible= (i == 0),
                line= dict(color= "red")
            )
        )
        stats_indices.append(len(fig.data) - 1)
        
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)+get_std(df, column)]*len(df[column]),
                name= 'Plus One Std Dev',
                visible= (i == 0),
                line= dict(color= "yellow")
            )
        )
        stats_indices.append(len(fig.data) - 1)
        
        fig.add_trace(
            go.Scatter(
                x= df['dates'],
                y= [get_mean(df, column)+ (2*get_std(df, column))]*len(df[column]),
                name= 'Plus Two Std Dev',
                visible= (i == 0),
                line= dict(color= "red")
            )
        )
        stats_indices.append(len(fig.data) - 1)
        
        stats_traces_indices.append(stats_indices)
    
    # Create dropdown menu
    buttons = []
    for i, column in enumerate(data_traces):
        visible_list = [False] * len(fig.data)
        # Show the data trace for the selected column
        visible_list[i] = True
        # Show the statistical traces for this parameter
        for stat_idx in stats_traces_indices[i]:
            visible_list[stat_idx] = True
        
        button = dict(
            label=column,
            method="update",
            args=[{"visible": visible_list}]
        )
        buttons.append(button)
    
    # Add dropdown menu to layout
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=buttons,
                direction="down",
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            )
        ]
    )
    
    return fig