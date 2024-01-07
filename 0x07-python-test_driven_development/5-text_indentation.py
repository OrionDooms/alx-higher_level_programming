#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these characters: ., ? and :.
    Args:
        text (str): takes in text.
    Raises:
        TypeError: text must be a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    characters = [".", "?", ":"]
    new_text = text
    for c in characters:
        new_text = new_text.replace(f'{c} ', f'{c}\n\n')
    print(new_text)
