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
import gensim
import part1
import part2

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

def stem_tokens(tokens:list):
    stemmer = PorterStemmer()
    # assume that all text has been cleaned and .lower()-ed
    return [stemmer.stem(token) for token in tokens]


def main():
    # PART 1
    random.seed(123)

    pg3300 = os.path.join(config.DATA_FOLDER, "pg3300.txt")
    log.assertion(os.path.exists(pg3300), "Data file not found")
    text = open(pg3300, "r", encoding="utf-8").read()

    with performance.Timer("Preprocess"):
        stemmed_paragraphs, original_paragraphs = part1.preprocess(text)
    
    with performance.Timer("Build Dictionary and Corpus"):
        dictionary, corpus = part2.build_dictionary_and_corpus(stemmed_paragraphs)


if __name__ == "__main__":
    main()