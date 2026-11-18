# -*- coding: utf-8 -*-

"""
Convert a text to a list of durations that alternatively represent dashes/dots
and blanks in Morse.



This list can then be passed as the `dashes` argument in Matplotlib's `plot()`
function, so that the lines looks likes Morse code. Theses durations can also be
used to style a stroke in Inkscape.


For example, 'test' will be converted to [3, 3, 1, 3, 1, 1, 1, 1, 1, 3, 3, 7]
which will be drawn as '___   _   _ _ _   ___       '


Note: For better results, with Matplotlib, the text should be no more than
a few (2-3 characters)

"""



from .alphabet import alphabet as alphabet_default
from .durations import durations_default





def text_to_symbols(text, alphabet=alphabet_default):
    """
    Converts a text to an intermediate language made of symbols ('.', '-', 
    extended with '_' and ' ')
    
    
    Parameters
    ----------
    text : string
        Text to convert to Morse symbols. Case insensitive.
    alphabet : dict, default=alphabet_default
        Dict describing how each character in the text should be encoded with 
        Morse symbols.
        
    Returns
    -------
    output : list[symbols]
        List of extended Morse symbols
        
    """
    
    # Convert to lower case (no difference between upper an lower in Morse)
    text = text.lower()
    
    
    # Some variables init
    output = ''
    
    n_chars = len(text)
    
    add_interletter = True
    
    inside_prosign = False
    
    
    # Check if there is an odd number of `~`
    # which means we have some messed up prosigns)
    if text.count('~')%2 == 1:
        raise ValueError("Cannot process prosigns: a tilda ('~') is missing " +
                         "somewhere to close a prosign.")
    
    
    # Replace each letter by the corresponding symbols
    for i in range(n_chars):
        
        
        # Process prosign formatting
        if text[i] == '~':
            # Toggle the state when entering/exiting
            inside_prosign = not(inside_prosign)
        
        # Or Add the Morse symbols corresponding to this char
        else:
            try:
             output += alphabet[text[i]]
            except:
                raise KeyError("Character '{0}' not in Morse alphabet".format(text[i]))
            
        
        # Whether to add an interletter pause or not
        
        # Never add one inside of a prosign
        if inside_prosign:
            add_interletter = False
            
        # Outside prosign: might add one, depending on the char
        # Note: when just exiting a prosign, we don't add a char (it's a '~'), 
        # but we still add a space, which is desired.
        else:
            # Default
            add_interletter = True
            
            # Not needed if the current char is a space
            if text[i]==' ':
                add_interletter = False
            
            # If the next char is a space, we also don't need it
            if (i+1<n_chars) and text[i+1] == ' ':
                add_interletter = False
            
        
        # Finally, add the interletter pause if needed
        if add_interletter:
            output += alphabet['interletter']

   
    
    return(output)
    

        

def symbols_to_dashes_length(symbols, alphabet=alphabet_default, durations=durations_default):
    """
    Convert an intermediate representation in symbols to the dashes and blanks
    of the correct durations.
    
    Parameters
    ----------
    symbols : list[symbols]
        List of extended Morse symbols
    alphabet : dict, default=alphabet_default
        Dict describing how each character in the text should be encoded with 
        Morse symbols.
    durations : dict, default=durations_default
        Dict describing the durations associated with the different Morse symbols
        and control characters.
        
    Returns
    -------
    output : list[int]
        List of durations, alternating between the duration of a line and the
        duration of a blank.
    
    """
    output = []
    n_symb = len(symbols)
    
    # For each symbol replace it by the corresponding symbol + intersymbol pause
    # (for letters/numbers only)
    for i in range(n_symb):
        s = symbols[i]
        
        # Interletter symbol
        if s == alphabet['interletter']:
            output.append(durations['interletter'])
            
        # Interword symbol (a space)
        elif s == alphabet[' ']:
            output.append(durations['interword'])
            
        # A dot or a dash
        else:
            output.append(durations[s])
            
            # If there is a dot or a dash next, we have to add and intersymbol space
            if (i+1) != n_symb:  
                if symbols[i+1]!='_' and symbols[i+1]!=' ':
                    output.append(durations['intersymbol'])
                
    
    return(output)



def text_to_dashes(text, alphabet=alphabet_default, durations=durations_default):
    """
    Convert a text to a list of durations that alternatively represent dashes/dots
    and blanks in Morse.
    

    Parameters
    ----------
    text : string
        Text to convert to Morse  code
    alphabet : dict, default=alphabet_default
        Dict describing how each character in the text should be encoded with 
        Morse symbols.
    durations : dict, default=durations_default
        Dict describing the durations associated with the different Morse symbols
        and control characters.
        
    Returns
    -------
    output : list[int]
        List of durations, alternating between the duration of a line and the
        duration of a blank.

    """
    
    # First, convert the text to Morse symbols
    symbols = text_to_symbols(text, alphabet)

    
    # Then, convert theses symbols to appropriate durations (with blanks)
    output = symbols_to_dashes_length(symbols, alphabet, durations)
    
    
    return(output)

