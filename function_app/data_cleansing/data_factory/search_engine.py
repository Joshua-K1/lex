import pandas as pd
from factory import load_profanity_data_frame

def search_input_for_profanity(input, profanity_df):
    print("Search input for profanity")

    profanity_df = profanity_df.str.lower()
    matches = [profanity_df.isin(input)]

    return matches

def search_input_for_undesired_tokens(input, undesired_tokens):
    print("Search input for undesired tokens")
    matches = [undesired_tokens.isin(input)]

    return matches