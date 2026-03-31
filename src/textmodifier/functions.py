from textmodifier.blockfont import FONT
import math

def block_text(text, scale=1):
    """
    Convert text to block font representation.
    
    Parameters:
    text (str): The input text to convert.
    scale (int): The scaling factor for the block font. Default is 1.
    
    Returns:
    str: Capitalized block font representation of the input text.

    Raises:
    TypeError: If text is not a string or scale is not an integer.
    ValueError: If scale is less than 1 or text contains unsupported characters.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(scale, int):
        raise TypeError("Scale must be an integer.")
    if scale < 1:
        raise ValueError("Scale must be at least 1.")

    spacing = max(1, scale//2)  # Calculate spacing based on scale
    text = text.upper()  # Convert text to uppercase

    for char in text:
        if char not in FONT:
            raise ValueError(f"Character '{char}' is not supported in block font.")

    if text == "":
        return ""
    character_height = len(FONT[text[0]])  # Get the height of the characters
    output = []

    for row in range(character_height):
        line_part = []

        for char in text:
            bitmap_row = FONT[char][row]
            rendered = ""

            for bit in bitmap_row:
                if bit == '1':
                    rendered += '#' * scale
                else:
                    rendered += ' ' * scale

            line_part.append(rendered)

        line = (" " * spacing).join(line_part)  # Join characters with spacing

        for _ in range(scale):  # Repeat each line according to the scale
            output.append(line.rstrip())  # Remove trailing spaces

    return "\n".join(output)

def remove_vowels(text, remove_y=False):
    """
    Remove vowels from the input text.
    
    Parameters:
    text (str): The input text from which to remove vowels.
    remove_y (bool): Whether to also remove 'y' and 'Y'. Default is False.
    
    Returns:
    str: The input text with vowels removed.

    Raises:
    TypeError: If text is not a string or remove_y is not a boolean.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(remove_y, bool):
        raise TypeError("remove_y must be a boolean.")

    vowels = "AEIOUaeiou"
    if remove_y:
        vowels += "Yy"
    return ''.join(char for char in text if char not in vowels)

def reverse_text(text):
    """
    reverse text for example "hello" becomes "olleh"

    Parameters:
    text(str): This is the input text to reverse

    Returns:
    the string text with order of letters reversed

    Raises:
    TypeError: If text is not a string
    """
    if not isinstance(text,str):
        raise TypeError("Reverse Test Function takes a string as an argument")
    length=len(text)
    if(text==""):
        return ""
    else:
        string1=""
        counter=length-1
        while(counter>=0):
            string1=string1+text[counter]
            counter=counter-1
        return string1

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
  