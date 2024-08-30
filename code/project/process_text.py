"""
Split the text into smaller paragraphs.
"""


def break_down_text():
    """
    Break down the text into a string and store each string and its length into a list.

    This function reads the entire content of a text file and returns a list containing
    the separated text as a single string and its length.

    :return: A list where the first element is the full text as a string, and the second element is the length of the text.
    """
    file_path = "../data/text_to_summarize.txt"
    with open(file_path, "r") as text:
        new_text = text.read()

    list_paragraphs = [new_text, len(new_text)]

    return list_paragraphs


def text_to_list():
    """
    Split the text into a list of paragraphs.

    This function reads the content of a text file, splits it into sections of text based on the delimiter '***',
    and strips any leading or trailing whitespace from each paragraph.

    :return: A list of paragraphs as strings, with leading and trailing whitespace removed.
    """
    file_path = "../data/text_to_summarize.txt"
    with open(file_path, "r") as text:
        new_text = text.read()

    list_paragraphs = new_text.split("***")
    list_paragraphs = [paragraph.strip() for paragraph in list_paragraphs]
    return list_paragraphs
