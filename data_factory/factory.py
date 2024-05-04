import json
import pandas as pd
import numpy as np
import logging
import pyodbc

logger = logging.getLogger()

def load_data():
    logger.info("Loading JSON data")
    with open('io/test_input.json') as f:
        data = json.load(f)
    
    return data


# Extract keys and data from json object
def load_keys(data):
    logger.info("Extracting keys and values from JSON data")
    extracted_values = []
    # Recursion checks if the object returned is a dictionary or a list
    for key in data.keys():
        if isinstance(data[key], dict):
            load_keys(data[key])
        if isinstance(data[key], list):
            for item in data[key]:
                if isinstance(item, list):
                    load_keys(item)
                if isinstance(item, dict):
                    load_keys(item)
                else:
                    extracted_values.append({"Key": key, "Value": item})
        else:
            extracted_values.append({"Key": key, "Value": data[key]})

    return extracted_values

# Create dataframe
def create_dataframe(extracted_values):
    keys = [item["Key"] for item in extracted_values]
    values = [item["Value"] for item in extracted_values]
    df = pd.DataFrame({"Key": keys, "Value": values, "Error": np.zeros(len(keys))})

    return df
