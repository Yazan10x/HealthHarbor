# adds a character ch for every character in str that is in chars
def add_slash(str: str, chars: str, ch: str): 
    for c in chars:
        s = str.replace(c, ch + c)
    return s