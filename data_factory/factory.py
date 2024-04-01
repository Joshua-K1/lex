import json
import csv


# load tokens and return new list with the word as the key
def load_undesired_tokens():
    print("Loading Undesired Tokens...")
    undesired_tokens_f = open('io/unsuitable.json')
    undesired_token_list = json.load(undesired_tokens_f)['words']

    return undesired_token_list


def create_undesired_token_index(token_list):
    print("undesired token index..")

    undesired_tokens_indexed = {token_list['word']: token for token in token_list}
    return undesired_tokens_indexed


def load_undesired_token_weights(token_list):
    print("Load undesired token weights...")

    token_weights = []
    for token in token_list:
        token_weights.append({
            "word": token['word'],
            "weight": token['weight']
        })

    return token_weights


# format raw inputs
def parse_raw_input():
    with open('io/input.txt') as f:
        lines = f.readlines()
        data = [line.replace(' ', '') for line in lines]

    return data 


def load_profanity_list():
    profanity_set = set()
    with open('io/profanity.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for word in row:
                profanity_set.add(word.lower())

    return profanity_set



