import re
import os
import sys

def clear_input(message=None):
    '''Clear the last line from the terminal and output a message
    '''
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.write(message)

def ask_for_sha256_or_file():
    '''Ask for SHA256 of File
    '''
    while True:
        reply = str(input('Enter a SHA256 or path to a File: ')).strip()
        input_type = validate_input(reply)
        if input_type:
            return reply, input_type
        clear_input(f'{reply} is not a valid SHA256 or File.\n')

def validate_input(string):
    if validate_file(string):
        return 'File'
    if validate_sha256(string):
        return 'SHA256'
    return False

def validate_sha256(string):
    '''Validate the SHA256
    '''
    match_obj = re.match(r"[a-fA-F0-9]{64}$", string)
    return bool(match_obj)

def validate_file(string):
    '''Validate the provided string is a file
    '''
    return os.path.isfile(string)

def main():
    ''' Main script logic
    '''
    try:
        user_input = sys.argv[1]
        input_type = validate_input(user_input)
        if not input_type:
            print(f'Provided argument {user_input} is not a valid SHA256 or File.')
            user_input, input_type = ask_for_sha256_or_file()
    except IndexError:
        user_input, input_type = ask_for_sha256_or_file()

    print(user_input)
    print(input_type)

if __name__ == '__main__':
    main()
