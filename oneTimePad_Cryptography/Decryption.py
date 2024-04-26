#taking the cipher message
cipher_message_input=input("\nInsert the cipher text:\n")

#taking the key to decrypt the message
key_input_raw=input("\nInsert the secret key:\n")

#to ensure that the key and the text are numbers
try:
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
