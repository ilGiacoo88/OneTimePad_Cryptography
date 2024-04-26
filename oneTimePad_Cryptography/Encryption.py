#Created by ilGiaco88
#Copyright© 2024 ilGiaco88
#License: MIT License
#Patch 0.0.1
#Version: 0.0.1
#Patch new features: the key is printed out as a hexadecimal number for a better user experience;the key, in the input, is taken as an hexadecimal number in the decryption; the input warns that you can't insert blank lines in the input()


#modules that we need in the project
import sys
import secrets

#variable for the loop
loop=True

#loop to ensure that the user has given us a message, if there wouldn't be this loop the program would crash
while loop:

    #user input message
    user_message=input("\nInsert the message to encrypt:\n")

    #saving user_message in a f variable
    original_message=f"{user_message}"

    #if statement to ensure that there's something in the message
    if(original_message!=""):
        #if there's the user_message the loop finishes
        loop=False
    else:
        #if there isn't the user_message, the loop continue
        continue

#transforming the original_message from string to binary, but the type is always string
message_str= '0b' + ''.join(format(ord(i), '08b') for i in original_message)

#transforming the message_str from string to number, from binary to decimal
message=int(message_str, 2)

#taking the size of the message in bytes, so we can use it for the secret key
message_size=sys.getsizeof(message)

#generating a key with the same number of bytes of the message, using the module secrets
key_raw=secrets.token_hex(message_size)

#changing the key_raw from hexadecimal to binary, but the type is always string
key_str= '0b' + ''.join(format(x, 'b') for x in bytearray(key_raw, 'utf-8'))

#changing the type of key_str from string to integers
key=int(key_str, 2)

#ciphering the text with the XOR operator
ciphertext= key ^ message

#WARNING
print("\nRemember the secret key and the ciphertext, because you will need them to decrypt the message later!")

#Secret Key
print("\nSecret key: \n" + str(key_raw))

#Ciphertext
print("\nCiphertext: \n" + str(bin(ciphertext)) + "\n")
