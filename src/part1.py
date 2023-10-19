#!/usr/bin/env python3

import string
from nltk.stem.porter import PorterStemmer
from nltk import FreqDist

def preprocess(text):
    # Storing original paragraphs for querying results later
    original_paragraphs = [p.strip() for p in text.split('\n\n') if p]

    # 3. Partitioning the loaded text into separate paragraphs & filtering "Gutenberg"
    original_paragraphs = [p for p in original_paragraphs if "gutenberg" not in p.lower() and p.strip() != ""]
    paragraphs = [p for p in original_paragraphs if p]

    # 4. Tokenizing paragraphs into individual words
    tokenized_paragraphs = [p.split() for p in paragraphs]

    # 5. Removing text punctuation and whitespaces and converting the text to lowercase
    def clean_tokens(tokens):
        return [token.lower().strip(string.punctuation + "\n\r\t") for token in tokens]

    cleaned_paragraphs = [clean_tokens(p) for p in tokenized_paragraphs]

    # 6. Using the PorterStemmer from NLTK to stem words
    stemmer = PorterStemmer()
    def stem_tokens(tokens):
        return [stemmer.stem(token) for token in tokens]

    stemmed_paragraphs = [stem_tokens(p) for p in cleaned_paragraphs]

    # 7. Using the FreqDist class of NLTK to see the count of specific words
    all_words = [word for paragraph in stemmed_paragraphs for word in paragraph]
    freq_dist = FreqDist(all_words)

    # Checking the frequency of the word "tax"
    # print(freq_dist["tax"])

    # Returning the list of processed paragraphs for querying purposes
    return stemmed_paragraphs, original_paragraphs
