from data_factory import factory
from language_processor import tokeniser as lp
from language_processor import profanity_filter
from better_profanity import profanity

def main():

    print("Main...")

    # load json data
    data = factory.load_data()

    # extract keys and values from json data
    extracted_values = factory.load_keys(data)

    # create dataframe
    df = factory.create_dataframe(extracted_values)

    keys_with_profanity = check_profanity(extracted_values)

    if keys_with_profanity is not None:
        for key in keys_with_profanity:
            print(key)
    else:
        print("No keys with profanity found...")


# check keys for profanity 
def check_profanity(input):
    print("Check for profanity...")
    keys_with_profanity = []
    for value in input:
        if isinstance(value['Value'], str):
            if profanity.contains_profanity(value['Value']):
                print(f"{value['Key']} contains profanity")

    
    return keys_with_profanity


if __name__ == "__main__":
    main()
