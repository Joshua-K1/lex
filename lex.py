from data_factory import factory as df
from language_processor import tokeniser as lp

def main():
    # load undesirable tokens
    undesired_token_list = df.load_undesired_tokens()
    unchecked_input = df.load_inputs()
    # load language processor object
    language_doc = lp.construct_language_doc(unchecked_input)
    print([token.text for token in language_doc])



if __name__ == "__main__":
    main()
