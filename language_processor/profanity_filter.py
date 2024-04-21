from better_profanity import profanity

def load_censor():
    print("Loading censor words..")
    return profanity.load_censor_words()

def check_profanity(text):
    print("Check profanity..")
    
    # returns True if profanity is found
    return profanity.contains_profanity(text)