# -*- coding: utf-8 -*-
"""
Morse alphabet
"""

# Morse alphabet (extended)
#
# Translates characters to dots and dashes 
# Taken from "Recommendation ITU-R M.1677-1 - International Morse Code" (10/2009 version)
#
# Compared to the real Morse code, this alphabet has been extended with two extra 'symbols' 
# - a space ' ', to represent a space between words
# - an underscore '_', to represent the small pause between to consecutive
#   letters inside of a word.

alphabet = { #Letters
            'a' : '.-',
            'b' : '-...',
            'c' : '-.-.',
            'd' : '-..',
            'e' : '.',
            'f' : '..-.',
            'g' : '--.',
            'h' : '....',
            'i' : '..',
            'j' : '.---',
            'k' : '-.-',
            'l' : '.-..',
            'm' : '--',
            'n' : '-.',
            'o' : '---',
            'p' : '.--.',
            'q' : '--.-',
            'r' : '.-.',
            's' : '...',
            't' : '-',
            'u' : '..-',
            'v' : '...-',
            'w' : '.--',
            'x' : '-..-',
            'y' : '-.--',
            'z' : '--..',
            # Accented letters
            'é' : '..-..',
            # Numbers
            '1' : '.----',
            '2' : '..---',
            '3' : '...--',
            '4' : '....-',
            '5' : '.....',
            '6' : '-....',
            '7' : '--...',
            '8' : '---..',
            '9' : '----.',
            '0' : '-----',
            # Punctuation and misc signs
            '.' : '.-.-.-', # Dot
            ',' : '--..--', # Comma
            ':' : '---...', # Colon or division sign
            '?' : '..--..', # Question mark
            "'" : '.----.', # Apostrophe
            '-' : '-..-.',  # Hyphen, dash, substraction sign
            '/' : '-..-.',  # Fraction bar, division sign, slash
            '(' : '-.--.',  # Opening parenthesis
            ')' : '-.--.-', # Closing parenthesis
            '"' : '.-..-.', # Quotation marks
            '=' : '-...-',  # Double hyphen, equal sign
            # 'x' : '-..-', # Multiplication. Same as x letter
            '@' : '.--.-.', # Commerical at
            # Extra symbols
            ' ' : ' ',
            'interletter': '_'}