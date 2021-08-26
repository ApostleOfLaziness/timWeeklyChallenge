text = input('What do you want to decipher?\n')

def decoder(text):
    if type(text) != str:
        raise TypeError('Please use a string')

    decoded = []
    cipher = range(0, len(text), 2)
    for pair in cipher:
        letter = int(text[pair]) * text[pair+1]
        decoded.append(letter.lower())

    print(decoded)


decoder(text)