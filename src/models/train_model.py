import numpy as np
import pandas as pd
import argparse
import os
import yaml
#from darts.models import XGBModel
# load data

def load_config(filename):
    """Loads project parameters

    Args:
        filename (dict): yaml file, containing project parameters

    Returns:
        dict : Dictionary with key, value pairs 
    """

    with open(filename) as f:
        config = yaml.safe_load(f) 
        return config

def _get_data(path):
    """Gets dataframe

    Args:
        path (string): Path for dataframe

    Returns:
        pd.DataFrame : Input dataframe  
    """

    return pd.read_csv(path,index_col="Id")
    

# Transformation pipeline


# Model

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="parameters.yaml")
    parsed_args = args.parse_args()
    print("parsed_arg",parsed_args.config)
    config_dict = load_config(parsed_args.config)

# get data
    df = _get_data(path=config_dict['data']['path'])
    print(df)
    

