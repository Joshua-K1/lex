from data_factory import factory
from language_processor import tokeniser as lp
from language_processor import profanity_filter

def main():
    pf = profanity_filter.load_censor()

    print("Main...")

    # load json data
    data = factory.load_data()

    # extract keys and values from json data
    extracted_values = factory.load_keys(data)

    df = factory.create_dataframe(extracted_values)
    print(df)



if __name__ == "__main__":
    main()
