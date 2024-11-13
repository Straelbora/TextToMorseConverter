from dictionary import MorseDictionary

morse_dict = MorseDictionary()


def convert_to_morse(user_input, dictionary):
    """Converts user input to Morse code and prints the result. Takes two arguments user_input and dictionary"""
    words = user_input.split()
    for word in words:
        for letter in word:
            print(f"{dictionary.get_code(letter.upper())} ", end=" ")


def decode_from_morse(user_input, dictionary):
    """Converts user input in Morse to letters and prints the result. Takes two arguments user_input and dictionary"""
    code = user_input.split('  ')
    for letter in code:
        print(f"{dictionary.get_letter(letter)}", end=" ")


is_working = True

while is_working:
    action = input('What do you want to do?:\n'
                   'convert - convert text to morse\n'
                   'show - show the morse dictionary\n'
                   'decode - decode a message from morse\n'
                   'end - ends the program\n')
    if action == 'convert':
        text = input('Enter the text you want to convert: \n')
        convert_to_morse(text, morse_dict)
        print("")
    elif action == 'show':
        morse_dict.show()
        print("")
    elif action == 'decode':
        print('Remember to put two spaces between each letter given in morse!')
        text = input('Enter the morse code to decode: \n')
        decode_from_morse(text, morse_dict)
        print("")
    elif action == 'end':
        print('Bye!')
        is_working = False
    else:
        print('Invalid command, please type one of the following:')
