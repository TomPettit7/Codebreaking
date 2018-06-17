key = 0

message = input('Message to Decrypt: \n')

def selectkey():
    global key
    key = input('Enter the key you want to try: \n')
    print('\n')

def decrypt():
    global key
    for symbol in message:
        if symbol.isalpha():
            numcode = ord(symbol)
            numcode -= int(key)
            if symbol.isupper():
                if numcode > ord('Z'):
                    numcode -= 26
                elif numcode < ord('A'):
                    numcode += 26
            elif symbol.islower():
                if numcode > ord('z'):
                    numcode -= 26
                elif numcode < ord('a'):
                    numcode += 26

        letter = chr(numcode)
        print(letter)

selectkey()
decrypt()
           
