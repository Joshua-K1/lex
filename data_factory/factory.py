import json
import csv
import pandas as pd

def load_data():
    print("Load Data...")
    with open('io/test_input.json') as f:
        data = json.load(f)
    
    return data


# Extract keys and data from json object
def load_keys(data):
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
    df = pd.DataFrame({"Key": keys, "Value": values})

    return df
