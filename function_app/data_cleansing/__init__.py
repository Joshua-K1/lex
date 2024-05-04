from .data_factory import factory
import azure.functions as func
from better_profanity import profanity
import logging

logging.basicConfig(filename="io/logfile.log", format='%(asctime)s - %(message)s', filemode='a')
logger = logging.getLogger()


def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.setLevel(logging.DEBUG)
    logger.info("Starting function run...")

    # load json data
    data = factory.load_data()

    # extract keys and values from json data
    extracted_values = factory.load_keys(data)

    # get id of submission
    submission_id = get_id(extracted_values)
    logger.info(f"Extracted values for submisson {submission_id}")

    df = factory.create_dataframe(extracted_values)

    # check each value for profanity
    keys_with_profanity = check_profanity(extracted_values)

    if len(keys_with_profanity) > 0:
        logger.info(f"Submission ID: {submission_id} | Status: Contains profanity | Moving to quarantine data store")
    else:
        logger.info(f"Submission ID: {submission_id} | Status: Clean | Moving to sanitised data store")

    return func.HttpResponse(
        "Function executed successfully. Check logs for more information.",
        status_code=200
    )


# check keys for profanity 
def check_profanity(input):
    logger.info(f"Checking for profanity for submission {get_id(input)}")

    keys_with_profanity = []

    for value in input:
        if isinstance(value['Value'], str):
            if profanity.contains_profanity(value['Value']):
                print(f"{value['Key']} contains profanity")
                keys_with_profanity.append({"Key": value['Key'], "Value": value['Value']})
    
    return keys_with_profanity


# get id of submission 
def get_id(input):
    for item in input:
        if item['Key'] == 'id':
            return item['Value']
        

if __name__ == "__main__":
    main()
