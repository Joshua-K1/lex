import json

# load tokens and return new list with the word as the key
def load_undesired_tokens():
    print("Loading Undesired Tokens...")
    undesired_tokens_f = open('io/unsuitable.json')
    undesired_tokens_data = json.load(undesired_tokens_f)['words']
    undesired_token_list = {undesired_token['word']: undesired_token for undesired_token in undesired_tokens_data}

    return undesired_token_list

# load input file
def load_inputs():
    print("Loading Inputs..")
    with open('io/input.txt', 'r') as input_f:
        unsanitised = input_f.read()
        return unsanitised
