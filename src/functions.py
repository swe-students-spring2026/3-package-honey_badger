from src.blockfont import FONT
import math


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
    

def fixed_length_encode(text, only_code=False, ignore_case=False, bit_style=("1", "0")) :
    """
    Encodes text using fixed length binary coding algorithm. It calculates the number of bits
    needed by using ceiling(log_2(n)), where n is the number of unique characters in the text. 
    This guarantees there is enough bits to represent all chars.

    Parameters:
    text (str): The input to encode
    only_code (bool): Boolean to decide if printing only code and no mapping. Default is False
    ignore_case (bool): Boolean to decide if ignoring capitalization. Default is False
    bit_style (tuple): Maps directly to (1, 0). Default is ("1", "0")

    Returns:
    str: Encoded text in custom bit style and optional mapping.

   
    """

    if not text:
        return ""

    if ignore_case:
        text = text.upper()

    chars = sorted(set(text))
    n = len(chars)
    bits = math.ceil(math.log2(n))
    codes = {}
    for i, c in enumerate(chars):
        codes[c] = bin(i)[2:].zfill(bits)


    out = ""
    
    for c in text:
        out += codes[c]

    if bit_style != ("1", "0"):
        mapping = {"1": bit_style[0], "0": bit_style[1]}
        out = "".join(mapping[bit] for bit in out)
        for char in codes:
            codes[char] = "".join(mapping[bit] for bit in codes[char])

    if only_code:
        return out
    else:
        return (str(codes) + "\n" + out)
    