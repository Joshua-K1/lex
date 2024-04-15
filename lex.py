from data_factory import factory as df
from language_processor import tokeniser as lp

def main():
    # load undesirable tokens
    undesired_token_list = df.load_undesired_tokens_df()

    # parse raw input, returns a list of strings
    # print statement prints new line characters, does this need removed?
    parse_raw_input = df.parse_raw_input()

    # tokenise input
    input_token_list = lp.tokenise_text(parse_raw_input) 

    for token_line in input_token_list:
        for item in token_line:
            if undesired_token_list['word'].str.contains(item):
                print(f"found undesired token {item}" )
        print(token_line)

    print(undesired_token_list)

    profanity_list = df.load_profanity_data_frame()
    #print(profanity_list)


if __name__ == "__main__":
    main()
