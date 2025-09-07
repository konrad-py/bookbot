#/usr/bin/env python3

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text: str) -> int:
    num_char = {}
    for l in text:
        if l.lower() in num_char:
            num_char[l.lower()] += 1
        else:
            num_char[l.lower()] = 1
    return num_char
