from data_factory import factory
from better_profanity import profanity

def main():

    print("Main...")

    # load json data
    data = factory.load_data()

    # extract keys and values from json data
    extracted_values = factory.load_keys(data)

    # get id
    id = get_id(extracted_values)
    print(f"ID of the submission: {id}")

    df = factory.create_dataframe(extracted_values)

    # check each value for profanity
    keys_with_profanity = check_profanity(extracted_values)

    if len(keys_with_profanity) > 0:
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
                keys_with_profanity.append({"Key": value['Key'], "Value": value['Value']})
    
    return keys_with_profanity


def get_id(input):
    for item in input:
        if item['Key'] == 'id':
            return item['Value']



if __name__ == "__main__":
    main()
