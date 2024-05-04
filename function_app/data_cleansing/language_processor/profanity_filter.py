from better_profanity import profanity
import logging

logger = logging.getLogger()

def load_censor():
    logger.info("Loading censor words")
    return profanity.load_censor_words()

def check_profanity(text):
    logger.info("Checking for profanity")
    
    # returns True if profanity is found
    return profanity.contains_profanity(text)