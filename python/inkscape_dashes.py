#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate numbers representing the length of dashes and blanks for styling strokes
 in Inkscape.
 
Usage :
    - Run this script
    - In Inkscape, go to the "Stroke style" tab
    - In the "Dashes" dropdown list, select "Custom". A new "Pattern" text input
      should appear.
    - Paste the output of this script in "Pattern"

"""

import argparse


from morseplot.text_to_dashes import text_to_dashes
import morseplot.durations as mdur


def generate_dashes_pattern(text, **kwargs):
    """
    Generate numbers representing the length of dashes and blanks for styling
    strokes in Inkscape.
    

    Parameters
    ----------
    text : string
        Text to translate to Morse
        
    alphabet : dict (optional)
        Dict describing how each character in the text should be encoded with 
        Morse symbols.
    durations : dict (optional)
        Dict describing the durations associated with the different Morse symbols
        and control characters.

    Returns
    -------
    pattern : string
        Pattern setting for Inkscape

    """
    
    # Get the list of durations (dot/dashes + blank)
    tmp = text_to_dashes(text, **kwargs)
    
    # Convert to a string, for copy-pasting into Inkscape
    pattern = ''.join(['{0:g}'.format(i)+' ' for i in tmp]) # g format to remove trailing zeros
    
    return(pattern)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="inkscape_dashes",
        description="Generate custom stroke dash-patterns for Inkscape")
    
    parser.add_argument("text")
    #parser.add_argument("-a", "--alphabet")
    parser.add_argument("-d", "--durations",
                        help="(Optional) " +
                             "Durations of the Morse symbols and pauses. " +
                             "Can either be 'default' (standard Morse Code), " +
                             "'shortened' (shorter pauses between letters/" +
                             "words, looks nicer) or a comma separated list" +
                             "of numbers with the following order: dot "+
                             " duration, dash duration, pause between " +
                             "dot/dashes, pause between letters, pause " +
                             " between words." +
                             "For example, standard Morse code (default), is " +
                             "equivalent to : 1,3,1,3,7 and the shortened " +
                             "option equivalent to : 1,3,1,2,3 (shorter " +
                             "pauses of duration 2 between letters and  3" +
                             "between words).")
    
    args = parser.parse_args()
    


    # Text verification

    # TODO
    


    # Durations string parsing and verification   
    # If no input was given, use the default.
    # Otherwise, parse the input string
    if not args.durations:
        durations = mdur.durations_default
    else:
        
        durations = mdur.parse_durations_multi_type(args.durations)



    # Compute the pattern for Inkscape dashes
    pattern = generate_dashes_pattern(args.text, durations=durations)
    
    
    # Simply print the result to the console
    print('Inkscape dashes pattern for "{0}":'.format(args.text))
    print(pattern)
    
