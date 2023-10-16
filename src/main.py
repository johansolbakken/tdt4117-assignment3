#!/usr/bin/env python3

import config
import os
import random
import codecs

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

def main():
    random.seed(123)

    pg3300 = os.path.join(config.DATA_FOLDER, "pg3300.txt")
    assert os.path.exists(pg3300), "Data file not found"

    paragraphs = make_paragraphs(pg3300)
    print(paragraphs)



if __name__ == "__main__":
    main()