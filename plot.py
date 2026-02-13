import plotly.graph_objects as go


def plot_graph(qc_df, stats_df):
    fig = go.Figure()

    data_traces = []
    data_traces_indices = []
    stats_traces_indices = [] 
    qc_columns= qc_df.columns.difference (['dates'], sort= False)  # exclude 'dates' column AND maintain original order!
 
    # Add statistics traces and track their indices
    std_levels = {
        1: {"name": "Mean ± 1 Std Dev", "line_color": "orange", "fill_color": "rgba(227, 96, 9, 0.75)"},
        2: {"name": "Mean ± 2 Std Dev", "line_color": "yellow", "fill_color": "rgba(227, 212, 9, 0.75)"},
        3: {"name": "Mean ± 3 Std Dev", "line_color": "red", "fill_color": "rgba(227, 9, 9, 0.6)"},
    }
    for i, column in enumerate(qc_columns): 
       mean, std = stats_df.loc[i, "Target Mean"], stats_df.loc[i, "SD"]
       stats_indices = []
       
       for level, features in std_levels.items():
           # Lower bound (no fill)
           fig.add_trace(
               go.Scatter(
                   x=qc_df["dates"],
                   y=[mean - (level * std)] * len(qc_df),
                   name=features["name"],
                   visible=(i == 0),
                   line=dict(color=features["line_color"], dash="solid"),
                   legendgroup=features["name"],
                   showlegend=False
               )
           )
           stats_indices.append(len(fig.data) - 1)
           
           # Upper bound
           fig.add_trace(
               go.Scatter(
                   x=qc_df["dates"],
                   y=[mean + (level * std)] * len(qc_df),
                   name=features["name"],
                   visible=(i == 0),
                   line=dict(color=features["line_color"], dash="solid"),
                   fill='tonexty',
                   fillcolor=features["fill_color"],
                   legendgroup=features["name"],
                   showlegend=(i == 0)
               )
           )
           stats_indices.append(len(fig.data) - 1)
   
       # Add mean line
       fig.add_trace(
           go.Scatter(
               x=qc_df["dates"],
               y=[mean] * len(qc_df),
               name="Mean",
               visible=(i == 0),
               line=dict(color="green", dash="solid"),
               legendgroup="Mean",
               showlegend=(i == 0)
           )
       )
       stats_indices.append(len(fig.data) - 1)

       stats_traces_indices.append(stats_indices)
    
    # Add data traces AFTER statistics so they appear on top
    for i, column in enumerate(qc_columns):  
        visible = (i == 0)  # first one visible
        fig.add_trace(
                      go.Scatter(
                      x=qc_df['dates'],
                      y=qc_df[column],
                      name=column,
                      visible=visible,
                      mode='lines+markers'
                  ))
        data_traces.append(column)
        data_traces_indices.append(len(fig.data) - 1)
    
    # Create dropdown menu
    buttons = []
    for i, column in enumerate(data_traces):
        visible_list = [False] * len(fig.data)
        # Show the statistical traces for this parameter
        for stat_idx in stats_traces_indices[i]:
            visible_list[stat_idx] = True
        # Show the data trace for the selected column
        visible_list[data_traces_indices[i]] = True
        
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