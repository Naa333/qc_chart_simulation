#generating functions for plotting graphs
import numpy as np
import pandas as pd
from load_ctrl_stats import load_stats

rng= np.random.default_rng(42)
def generate_data(stats_df, num_of_entries, rng=rng):
    #loop and generate data for each column name (dict)
    #if data type of data range = int, use int random generator
    #else use float
    analytes, means, stds= stats_df.loc[:, "Analyte"], stats_df.loc[:, "Target Mean"], stats_df.loc[:, "SD"]
    data_dict= {}
    for i, column_name in enumerate(analytes):
        mean= means[i]
        std= stds[i]
        if isinstance(mean, int):
            values= rng.integers(
                            low= mean - std, 
                            high= mean + std, 
                            size= num_of_entries
                                )
        else:
            values= np.round(
                            rng.uniform(
                            low= mean - std, 
                            high= mean + std, 
                            size= num_of_entries),
                        1
                        )
        data_dict[column_name] = values
    return data_dict
