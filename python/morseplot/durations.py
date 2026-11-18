# -*- coding: utf-8 -*-
"""
Durations of the different Morse symbols and control characters
"""





# Standard Morse code durations
durations_default = {# Morse symbols
                     '.' : 1,
                     '-' : 3,
                     # Control characters
                     'intersymbol' : 1, # Pause between dashes and dots that are part of the same letter
                     'interletter' : 3, # Pause between two distincts letters
                     'interword' : 7} # Pause between two words





# Variant with shorter durations for the interletter and interword pauses so
# that it looks nicer
durations_shortened = {# Morse symbols
                       '.' : 1,
                       '-' : 3,
                       # Control characters
                       'intersymbol' : 1, # Pause between dashes and dots that are part of the same letter
                       'interletter' : 2, # Pause between two distincts letters
                       'interword' : 3} # Pause between two words






def parse_durations_multi_type(durations_in):
    
    """
    Input parsing for durations coming from various sources (code, from the 
    command line, ...) in different formats/types.
    
    Checks that the values are correct and constructs a valid durations dict
    
    Parameters
    ----------
    durations_in : None, dict, str, list[float|int]
        Inputs to check. Accepted values/types are :
                - None for default durations
                - A dict that corresponds to the spec (see durations_default
                for an example)
                - A string, either 'default', 'shortened' or a comma separated
                list of values
                - A list of floats/ints with the correct number of elements
    
    Returns
    -------
    durations : dict
        A dict that respects the specs (see durations_default for an example)
    
    """
    
    symbols = ['.', '-', 'intersymbol', 'interletter', 'interword']
    

    
    if durations_in is None:
        durations = durations_default
    
    
    # If the input durations is a dict, we need to check:
    # - That it has the correct number of keys
    # - That the keys correspond to the symbols
    elif isinstance(durations_in, dict):
        keys = durations.keys()
        
        # Check for number of keys
        if len(keys) != 5:
            raise ValueError('Incorrect number of keys in durations dict')
            
        # Check for keys correctness
        missing_key = False
        
        for symb in symbols:
            if symb not in keys:
                missing_key = False
                break
        
        if missing_key:
            raise ValueError(f'Missing info for symbol {symb} in the durations dict')
    
        durations = durations_in
    
    # If the input is a string, we need to check, that it has the correct
    # number of elements. And then copy the values to a dict
    elif isinstance(durations_in, list):
        
        if len(durations_in) != 5:
            raise ValueError('Incorrect number of keys in durations list')
        
        
        # Create the durations dict
        durations = {# Morse symbols
                    '.' : durations_in[0],
                    '-' : durations_in[1],
                    # Control characters
                    'intersymbol' : durations_in[2], # Pause between dashes and dots that are part of the same letter
                    'interletter' : durations_in[3], # Pause between two distincts letters
                    'interword' : durations_in[4]} # Pause between two words
    
    
    # Durations can also be a string, for example if we want to use some
    # known settings ('default' or 'shortened') or we got the values from
    # the command line
    elif isinstance(durations_in, str):
        
        # Remove extra spaces
        durations_in = durations_in.strip()
        
        # Empty string
        if not durations_in:
            raise ValueError('Durations string cannot be empty/only whitespace. ' +
                             'Use None instead if you want to use the ' +
                             'default values')
        
        
        # A string and not a list (approx ...)
        elif durations_in.isalnum(): 
            if durations_in == 'default':
                durations = durations_default
                
            elif durations_in == 'shortened':
                durations = durations_shortened
            else:
                raise ValueError('Unknow duration option: {0}'.format(durations_in))
        
        # A list of comma separated numbers (Hopefully. If not, errors will be raised)
        else:
            try:
                
                dur_str_list = durations_in.strip(" \n\r").split(',')
                
                
                if len(dur_str_list) != 5:
                    raise ValueError('Incorrect number of durations: {0} instead of 5'.format(len(dur_str_list)))
                
                dur = []
                
                # Cast to floats
                for duration in dur_str_list:
                    dur_float = float(duration)

                    dur.append(dur_float)
                    
                # Create the durations dict
                durations = {# Morse symbols
                            '.' : dur[0],
                            '-' : dur[1],
                            # Control characters
                            'intersymbol' : dur[2], # Pause between dashes and dots that are part of the same letter
                            'interletter' : dur[3], # Pause between two distincts letters
                            'interword' : dur[4]} # Pause between two words
            
            except Exception:
                raise
                
    else:
        raise ValueError('Incorrect durations type')
        
        
    # Last step, for every type of input, verify that the durations are 
    # actually positive
    for symb, val in durations.items():
        if val <= 0:
            raise ValueError(f'Duration for {symb} is incorrect: {val}. It must be positive.')
        

            
    return(durations)