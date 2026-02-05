 #generating functions for plotting graphs
#create a dummy df of values I can plot
import numpy as np
import pandas as pd
import plotly.graph_objects as go

rng= np.default_range(42)
def generate_data(column_name, data_range, num_of_entries, rng):
    #loop and generate data for each column name (dict)
    #if data type of data range = int, use int random generator
    #else use float
    if isinstance(data_range[0], int):
        values= rng.integers(
                        low= data_range[0], 
                        high= data_range[-1], 
                        size= num_of_entries
                            )
    else:
        values= np.round(
                        rng.uniform(
                         low= data_range[0], 
                         high= data_range[-1], 
                         size= num_of_entries),
                       1
                       )
    return {column_name: values}

def build_df(data_dict, start_date): #num_of_entries has to be the same
    df = pd.DataFrame(data_dict)
    #add date column. Generate a sequence of dates from the specified date daily, 'D', up to the length of vertical cols
    df['dates']= pd.date_range(
                         start= start_date, 
                         periods= len(df.index), 
                         freq= 'D'
                         ) 
    return df

def compute_stats(df, column_name):
    mean= df[column_name].mean() 
    std= df[column_name].std()
    return mean, std
 


def plot_graph(df):
    fig = go.Figure()

    data_traces = []
    stats_traces_indices = [] 
    columns= df.columns.difference (['dates'])  # exclude dates
 
    for i, column in enumerate(columns):  
        visible = (i == 0)  # first one visible
        fig.add_trace(
                      go.Scatter(
                      x=df['dates'],
                      y=df[column],
                      name=column,
                      visible=visible
                  )
        data_traces.append(column)

    # Add statistics traces and track their indices
   std_levels= {
    -2: {"color": "red", "name": "Minus Two SD"},
    -1: {"color": "yellow", "name": "Minus One SD"},
     0: {"color": "green", "name": "Mean"},
     1: {"color": "yellow", "name": "Plus One SD"},
     2: {"color": "red", "name": "Plus Two SD"}
    }
    for i, column in enumerate(columns): 
       mean, std = compute_stats(df, column)
       stats_indices = []
   
       for level, features in std_levels.items():
           fig.add_trace(
               go.Scatter(
                   x=df["dates"],
                   y=[mean + level * std] * len(df),
                   name=features["name"],
                   visible=(i == 0),
                   line=dict(color=features["color"], dash="dash")
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
        plot_bgcolor='white',
        title="QC Parameter Trends with Statistics",
        xaxis_title="Date",
        yaxis_title="Value",
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
