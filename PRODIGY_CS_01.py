letters = 'abcdefghijklmnopqrstuvwxyz' #defines a variable named letters and assigns it a string 


def encrypt(plaintext, key):    #define a function named encrypt 
    ciphertext = ''  # Use an empty string for concatenation to store the encrypted text 
    for letter in plaintext:        #for loop that iterates through each char
        letter = letter.lower()     #convert the letters to lower case
        if letter.isalpha():  # Check if it's a letter from a to z
            index = letters.find(letter)          #search for position(index) of the current letter with string
            if index != -1:          #check if the index found in the previous step is not -1 
                new_index = (index + key) % 26  # Use modulo for wrapping
                ciphertext += letters[new_index]
        else:
            ciphertext += letter  # Preserve non-alphabetic characters

    return ciphertext        #after the loop iterates Return the final ciphertext char


def decrypt(ciphertext, key):          #define a function named decrypt 
    plaintext = ''                   # Use an empty string for concatenation to store the encrypted text
    for letter in ciphertext:        #for loop that iterates through each char
        letter = letter.lower()      #convert the letters to lower case
        if letter.isalpha():         # Check if it's a letter from a to z
            index = letters.find(letter)    #search for position(index) of the current letter with string
            if index != -1:                      #check if the index found in the previous step is not -1
                new_index = (index - key) % 26         #Use modulo for wrapping
                plaintext += letters[new_index]
        else:
            plaintext += letter

    return plaintext             #after the loop iterates Return the final plaintext char


print()         #print an empty line
print('---CEASER CIPHER---')
print()         #print an empty line
print('Do You Want Encryption or Decryption?')
user_input = input('e/d: ').lower()         #take the input from user and convert to lower case 
                                            #('e/d: ') this part takes the input from user and store it

if user_input == 'e':           
    print('You chose encryption')
    print()
    key = int(input('Enter the Key (1 through 26): '))     #ask the user to enter the shift amount for encryption
    text = input('Enter the text to encrypt: ')            #ask the user to enter the text to encrypt
    ciphertext = encrypt(text, key)                  #call the encrypt function
    print(f'CipherText: {ciphertext}')               #print the encrypted text 

elif user_input == 'd':
    print('You chose decryption')
    print()
    key = int(input('Enter the Key (1 through 26): '))      #ask the user to enter the shift amount for decryption
    text = input('Enter the text to decrypt: ')             #ask the user to enter the text to decrypt
    plaintext = decrypt(text, key)                   #call the decrypt function
    print(f'PlainText: {plaintext}')                 #print the decrypted text

else:
    print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")    #an error msg to inform the user that the inout is not valid