# adds a string str_add behind every character in str that is in chars
def add_string(str: str, chars: str, str_add: str): 
    for c in chars:
        s = str.replace(c, str_add + c)
    return s