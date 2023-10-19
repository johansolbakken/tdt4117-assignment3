import gensim
from gensim import corpora
import log
import config
import os

# Assuming processed_paragraphs is already loaded from previous code

def build_dictionary_and_corpus(processed_paragraphs):
    # 1. Build a dictionary from processed paragraphs
    dictionary = corpora.Dictionary(processed_paragraphs)
    
    # 2. Filtering out stopwords using provided list
    stopwords_file = os.path.join(config.DATA_FOLDER, "stopwords.csv")
    log.assertion(os.path.exists(stopwords_file), "Data file not found")
    stopwords = open(stopwords_file, "r", encoding="utf-8").read().split(",")
    
    stop_ids = [dictionary.token2id[stopword] for stopword in stopwords if stopword in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)
    
    # 3. Map paragraphs into Bags-of-Words using the constructed dictionary
    corpus = [dictionary.doc2bow(text) for text in processed_paragraphs]

    # Return dictionary and corpus for future use
    return dictionary, corpus