#!/usr/bin/env python3
from stats import *
import sys

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()


def main():
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    num_char = get_num_characters(text)
    for x in sorted(num_char, key=lambda x: num_char[x], reverse=True):
        if x.isalnum():
            print(f'{x}: {num_char[x]}')
    print('============= END ===============')
    



if __name__ == '__main__':
    main()

