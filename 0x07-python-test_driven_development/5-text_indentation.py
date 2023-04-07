#!/usr/bin/python3
# Text indentation

''' A function that prints a text with 2 new lines after
each of these characters: ., ? and : '''


def text_indentation(text):
    """defines a function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = text.replace('.', '.\n\n')
    new_text = text.replace('?', '?\n\n')
    new_text = text.replace(':', ':\n\n')
    new_text = text.replace('\n ', '\n\n')

    """Splitting the lines before separating each """
    n_lines = new_text.split('\n')
    for line in n_ines:
        # strip any leading or trailing whitespace from the line
        line = line.strip()
        print(line)
