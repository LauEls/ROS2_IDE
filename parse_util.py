import re
from io import TextIOWrapper

def preProcess(file: TextIOWrapper) -> str:
    """
    Removes comments from a file and returns the file as a string.
    """

    lines = file.readlines()

    for i, line in enumerate(lines):
        match = re.search("#", line)

        if match is not None:
            lines[i] = line[0:match.start()]

    out = ''.join(lines)
    return out

def findChar(string: str, start_index: int, target_char: str) -> int:
    """
    Returns the index of the first occurence of target_char in string after start_index.
    """
    
    i = start_index
    while string[i] != target_char:
        i += 1

    return i