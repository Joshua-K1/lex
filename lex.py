from data_factory import factory as df
from language_processor import tokeniser as lp

def main():
    # load undesirable tokens
    undesired_token_list = df.load_undesired_tokens()

    # parse raw input
    parse_raw_input = df.parse_raw_input()

    # load language processor object
    #language_doc = lp.construct_language_doc(parse_raw_input)

    # create token list
    #token_list = [token.text for token in language_doc]

    # load weights
    weights = df.load_undesired_token_weights(undesired_token_list)


if __name__ == "__main__":
    main()
