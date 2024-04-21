import json
import csv
import pandas as pd

def load_data():
    print("Load Data...")
    with open('io/test_input.json') as f:
        data = json.load(f)
    
    return data


def load_keys(data):
    for key in data.keys():
        #print(f"Key Name: {key}" + f" Key Value: {data[key]}")

        if isinstance(data[key], dict):
            load_keys(data[key])

        if isinstance(data[key], list):
            for item in data[key]:
                if isinstance(item, list):
                    load_keys(item)

                if isinstance(item, dict):
                    load_keys(item)

                else:
                    print(f"{item}")
        else:
            print(data[key])
