'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

class AlgorithmicException(Exception):
    pass

class KeyRangeException(Exception):
    pass

try:
    algorithm = input('Do you want to (e)ncrypt or (d)ecrypt? \n > ')
    if (algorithm == 'e'):
        key = int(input('Please enter the key (0 to 25) to use. \n > '))
    elif (algorithm == 'd'):
        key = int(input('Please enter the key (0 to 25) to use. \n > '))
    else:
        raise AlgorithmicException

    if (key < 0 or key > 25):
        raise KeyRangeException

    if (algorithm == 'e'):
        message = input('Enter the message to encrypt. \n > ')
    else:
        message = input('Enter the message to decrypt. \n > ')

    message = message.upper()

    modified_message = ''
    for i in range(len(message)):

        if (ord(message[i]) >= 65 and ord(message[i]) <= 90):
            if (algorithm == 'e'):
                value = ord(message[i]) + key
            else:
                value = ord(message[i]) - key

            if (value > ord('Z')):
                value -= 26

            if (value < ord('A')):
                value += 26

            modified_message += chr(value)

        else:
            modified_message += message[i]

    print(modified_message)
    
except AlgorithmicException:
    print ('You can do only (e)ncrypt or (d)ecrypt')
except KeyRangeException:
    print ('Key needs to be from 0 to 25')
except ValueError:
    print ('Can not use any text for key')
except Exception:
    print ('Unusual Exception Occurred')