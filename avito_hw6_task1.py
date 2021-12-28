from morze import *
import doctest


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе
    >>> encode('SOS')
    '... --- ...'
    >>> assert encode('SOS') == '... --- ...'
    >>> encode('PLEASE HELP. WE NEED FIRST AID.')
    '.--. .-.. . .- ... .   .... . .-.. .--. .-.-.-
       .-- .   -. . . -..   ..-. .. .-. ... -   .- .. -.. .-.-.-'
    >>> encode('SOS')
    '... ... ...'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
