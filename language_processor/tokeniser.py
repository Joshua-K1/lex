import nltk

# does this need to be loaded every time?
nltk.download('punkt')

def tokenise_text(data):
    tokenised_data = [nltk.word_tokenize(token) for token in data]

    return tokenised_data
