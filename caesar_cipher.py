import string


def caesar_cipher(text, key, encode=True):
    alpha_low = string.ascii_lowercase
    alpha_up = string.ascii_uppercase
    encoded_text = ''
    for t in text:
        if t in alpha_low:
            ind = (alpha_low.find(t) + key) % 26 if encode else (alpha_low.find(t) - key) % 26
            encoded_text += alpha_low[ind]
        elif t in alpha_up:
            ind = (alpha_up.find(t) + key) % 26 if encode else (alpha_up.find(t) - key) % 26
            encoded_text += alpha_up[ind]
        else:
            encoded_text += t

    return encoded_text


def pass_value():
    try:
        num = int(input('Enter a number between 1 and 25: '))
        if num < 1 or num > 25:
            print('Please enter a valid number.')
            return
        text = input('Enter a text: ')
        mode = input('Choose a mode: [e/d] ').lower()
        if mode not in ['e', 'd']:
            print('Invalid mode. Choose "e" for encode and "d" for decode.')
            return
        m = True if mode == 'e' else False
        result = caesar_cipher(text, num, m)
        print(f'Result: {result}')
    except ValueError:
        print('Please enter valid number.')


if __name__ == '__main__':
    pass_value()
