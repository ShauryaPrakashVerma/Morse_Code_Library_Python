from .utils import build_lookup

LOOKUP = build_lookup()

def encode(input_msg) -> str:
    
    """
    Encode a string into Morse Code

    Args:
        input_msg (str): The text to be converted into Morse Code.

    Returns:
        str: A string of dots and dashes i.e. the morse code of the input string.
    """
    
    final_msg = []
    
    for char in input_msg.upper():
        if char in LOOKUP:
            final_msg.append(LOOKUP[char])
        else:
            raise ValueError(f"Character '{char}' not supported.")
    
    return " ".join(final_msg)
        
        

