from .utils import build_reverse_lookup

def decode(morse_str="... --- ...", language = "english") -> str:
    language = language.lower()
    reverse_lookup = build_reverse_lookup(language)
    
    result = []
    
    for symbol in morse_str.split():
        if symbol == "/":
            result.append(" ")
        elif symbol in reverse_lookup:
            result.append(reverse_lookup[symbol])
        else:
            raise ValueError(f"Morse '{symbol}' not recognized")

    return "".join(result)
