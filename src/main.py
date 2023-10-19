#!/usr/bin/env python3

import config
import os
import random
import codecs
import string
import performance
import log
from nltk.stem.porter import PorterStemmer
import nltk

def make_paragraphs(text:str) -> list:
    paragraphs = []
    with codecs.open(text, "r", encoding="utf-8") as f:
        lines = f.readlines()
        paragraph = ""
        for line in lines:
            if line.strip() == "":
                if paragraph.strip() != "":
                    paragraphs.append(paragraph.strip())
                paragraph = ""
            else:
                paragraph += line
    return paragraphs

def filter_out(paragraphs, func) -> list:
    return [p for p in paragraphs if func(p)]

def clean_text(text:str): 
    cleaned_text = ''.join(char for char in text if char not in string.punctuation)
    cleaned_text = ' '.join([term.strip() for term in cleaned_text.split()])
    return cleaned_text.lower()  

def remove_stopwords(tokens:list):
    stopwords = os.path.join(config.DATA_FOLDER, "stopwords.txt")
    log.assertion(os.path.exists(stopwords), "Stopwords file not found")
    
    with codecs.open(stopwords, "r", encoding="utf-8") as f:
        lines = f.readlines()
        stopwords = [line.strip() for line in lines]
    return [token for token in tokens if token not in stopwords]

def stem_tokens(tokens:list):
    stemmer = PorterStemmer()
    # assume that all text has been cleaned and .lower()-ed
    return [stemmer.stem(token) for token in tokens]

def main():
    # PART 1
    random.seed(123)

    pg3300 = os.path.join(config.DATA_FOLDER, "pg3300.txt")
    log.assertion(os.path.exists(pg3300), "Data file not found")

    with performance.Timer("Make paragraphs"):
        paragraphs = make_paragraphs(pg3300)
    with performance.Timer("Filter out gutenberg"):
        paragraphs = filter_out(paragraphs, lambda p: not "gutenberg" in p.lower())
        original_paragraphs = [p for p in paragraphs]
    with performance.Timer("Clean text"):
        paragraphs = [clean_text(p) for p in paragraphs]
    with performance.Timer("Tokenize"):
        paragraphs = [p.split(" ") for p in paragraphs]
    with performance.Timer("Stem words"):
        paragraphs = [stem_tokens(p) for p in paragraphs]

    frequencies = nltk.FreqDist([token for paragraph in paragraphs for token in paragraph])

    # PART 2

if __name__ == "__main__":
    main()