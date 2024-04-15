import json
import csv
import pandas as pd


# load undesired tokens and create a data frame
def load_undesired_tokens_df():
    undesired_tokens_f = open('io/unsuitable.json')
    undesired_token_list = json.load(undesired_tokens_f)['words']
    undesired_words = [word['word'] for word in undesired_token_list]
    # convert words to lower case
    undesired_words = [word.lower() for word in undesired_words]
    udesired_categories = [word['category'] for word in undesired_token_list]
    undesired_weights = [word['weight'] for word in undesired_token_list]
    data = {
        'word': undesired_words,
        'category': udesired_categories,
        'weight': undesired_weights
    }

    df = pd.DataFrame(data)

    return df

# format raw inputs
def parse_raw_input():
    data = []
    with open('io/input.txt') as f:
        lines = f.readlines()
        data = [line for line in lines if line.strip()]

    return data


def load_profanity_data_frame():
    print("Loading profanity data frame")
    df = pd.read_csv('io/profanity.csv')

    return df


def load_profanity_list():
    profanity_set = set()
    with open('io/profanity.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for word in row:
                profanity_set.add(word.lower())

    return profanity_set
