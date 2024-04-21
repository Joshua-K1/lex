from better_profanity import profanity

def load_censor():
    print("Loading censor words..")
    return profanity.load_censor_words()
    