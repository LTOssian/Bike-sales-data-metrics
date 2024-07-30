#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print(word, separator, '1')

if __name__ == "__main__":
    main()
