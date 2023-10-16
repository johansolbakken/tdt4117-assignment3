#!/usr/bin/env python3

import config
import os

def main():
    assert os.path.exists(config.DATA_FOLDER), "Data folder not found"

if __name__ == "__main__":
    main()