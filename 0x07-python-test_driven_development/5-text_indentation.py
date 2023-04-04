#!/usr/bin/python3
# Text indentation

def text_indentation(text):
    """defines a function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = text.replace('.', '.\n')
    new_text = new_text.replace('?', '?\n')
    new_text = new_text.replace(':', ':\n')
    new_text = new_text.replace('\n ', '\n')
    print(new_text)
