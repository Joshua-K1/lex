from data_factory import factory as df
from language_processor import tokeniser as lp
from language_processor import profanity_filter

def main():
    pf = profanity_filter.load_censor()

    print("Main...")

    # load json data
    data = df.load_data()

    df.load_keys(data)

if __name__ == "__main__":
    main()
