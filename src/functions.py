from src.blockfont import FONT

def block_text(text, scale=1):
    """
    Convert text to block font representation.
    
    Parameters:
    text (str): The input text to convert.
    scale (int): The scaling factor for the block font. Default is 1.
    
    Returns:
    str: Capitalized block font representation of the input text.
    """
    spacing = max(1, scale//2)  # Calculate spacing based on scale
    text = text.upper()  # Convert text to uppercase

    for char in text:
        if char not in FONT:
            raise ValueError(f"Character '{char}' is not supported in block font.")

    if text == "":
        return ""

def reverse_text(text):
    length=len(text)
    string1=""
    counter=length-1
    while(counter>=0):
        string1=string1+text[counter]
        counter=counter-1
    return string1
