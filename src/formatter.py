import re


def formatter(string, index=None):
    if index is not None:
        print(index, "!!!!!!!!!!!!!!")
    new_string = string.replace("—", " — ")
    new_string = new_string.replace("×", " × ")
    new_string = new_string.replace("=", " = ")
    new_string = new_string.replace("/", " / ")
    new_string = new_string.replace("из", " из ")

    pattern_html_tags = r"(\<[^>]+>)|([\t]+)|([\n\r]+)"
    new_string = re.sub(pattern_html_tags, "", new_string)

    pattern_one_space = r"([\s]{2,})"
    new_string = re.sub(pattern_one_space, " ", new_string)

    pattern_word_space_number = r"(\d)([A-Za-zА-Яа-я])"
    repl_word_space_number = r"\1 \2"
    new_string = re.sub(pattern_word_space_number, repl_word_space_number, new_string)
    pattern_word_space_number = r"([A-Za-zА-Яа-я])(\d)"
    repl_word_space_number = r"\1 \2"
    new_string = re.sub(pattern_word_space_number, repl_word_space_number, new_string)

    return new_string