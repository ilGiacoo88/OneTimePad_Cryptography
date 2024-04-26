#Created by ilGiaco88
#Copyright© 2024 ilGiaco88
#License: MIT License
#Patch 0.0.1
#Version: 0.0.1
#Patch new features: the key is printed out as a hexadecimal number for a better user experience; the key, in the input, is taken as an hexadecimal number in the decryption; the input warns that you can't insert blank lines in the input()


#taking the cipher message
cipher_message_input=input("\nInsert the cipher text:\n")

#taking the key to decrypt the message
key_input_raw=input("\nInsert the secret key:\n")

#try/except to ensure that the key and the text are numbers and not other invalid types
try:
    #transforming the key from hexadecimal to binary
    key_input_raw= '0b' + ''.join(format(x, 'b') for x in bytearray(key_input_raw, 'utf-8'))

    #transforming the cipher message from string to integers
    cipher_message=int(cipher_message_input, 2)

    #transforming the key from string to integers
    key=int(key_input_raw, 2)

    #decrypting the cipher text with the key, the result is in decimal
    decimal_message= cipher_message ^ key

    #function to transform the decimal number into binary number
    def decimalToBinary(n): 
        return "{0:b}".format(int(n))
    
    #transforming the binary_message from decimal to binary
    message_binary= decimalToBinary(decimal_message)

    #transforming binary number into the utf-8 letters
    message_utf=int(message_binary, 2).to_bytes((len(message_binary) + 7) // 8, 'big')

    #transforming the message_utf from binary string to string
    message=message_utf.decode('utf-8')
    
    #printing the message decrypted
    print("\nThe decrypted message is:")
    print(message)
    print("\n")

#if the type is not a number, the program doesn't crash
except:
    print("You must insert numbers in the inputs, any other data type are not accepted")
