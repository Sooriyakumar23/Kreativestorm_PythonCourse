'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

def cipher_decrypt(cipher_text, key):
    plain_text = ''
    for index, character in enumerate(cipher_text):
        if (character == ' '):
            plain_text += character
            continue

        value = ord(character) - key
        
        if (value > ord('Z')):
            value -= 26

        if (value < ord('A')):
            value += 26

        plain_text += chr(value)

    return (plain_text)

cipher_text = input("Enter the cipher text to try brute force: ") # QIIX QI FC XLI VSWI FYWLIW XSRMKLX

print ('\nPossible plain texts for the cipher text you provided are: \n')

for key in range(26):
    plain_text = cipher_decrypt(cipher_text.upper(), key)
    print (plain_text)