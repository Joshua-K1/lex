import re
import spacy

def create_spacy_tokeniser():
    language_processor = spacy.load("en_core_web_sm")
    
    return language_processor


def construct_language_doc(data):
    lp = create_spacy_tokeniser()
    language_doc = lp(data)

    return language_doc



