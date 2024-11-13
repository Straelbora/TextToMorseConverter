import pprint

MORSE_DICTIONARY = {'A': '• -',
                    'B': '- • • •',
                    'C': '- • - •',
                    'D': '- • •',
                    'E': '•',
                    'F': '• • - •',
                    'G': '- - •',
                    'H': '• • • •',
                    'I': '• •',
                    'J': '• - - -',
                    'K': '- • -',
                    'L': '• - • •',
                    'M': '- -',
                    'N': '- •',
                    'O': '- - -',
                    'P': '• - - •',
                    'Q': '- - • -',
                    'R': '• - •',
                    'S': '• • •',
                    'T': '-',
                    'U': '• • -',
                    'V': '• • • -',
                    'W': '• - -',
                    'X': '- • • -',
                    'Y': '- • - -',
                    'Z': '- - • •',
                    '1': '• - - - -',
                    '2': '• • - - -',
                    '3': '• • • - -',
                    '4': '• • • • -',
                    '5': '• • • • •',
                    '6': '- • • • •',
                    '7': '- - • • •',
                    '8': '- - - • •',
                    '9': '- - - - •',
                    '0': '- - - - -',
                    }


class MorseDictionary:

    def __init__(self):
        self.dictionary = MORSE_DICTIONARY

    def get_code(self, letter):
        """Takes the letter as input and returns the code in Morse for that letter"""
        return self.dictionary[letter]

    def show(self):
        """Displays the Morse dictionary"""
        pprint.pprint(self.dictionary)

    def get_letter(self, code):
        """Takes the letter code in Morse and returns the actual letter"""
        for (key, value) in self.dictionary.items():
            if value == code:
                return key
