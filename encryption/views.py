
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

#function to encrypt the message
def encrypt(request):
    plaintext = request.GET.get('text', 'default')
    ciphertext = '' #the ciphertext to be returned, initially assigned to an empty string
    if(len(plaintext)): 
        for character in plaintext:   
            if (character.isupper()) :
                ciphertext+=chr(90-(ord(character)-65)%26 )#if character is uppercase, then modify the sum
            elif character == " ":
                #if the character is space then it is appended as it is
                ciphertext+=" "
            elif (character.islower() ):
                ciphertext+=chr(122-(ord(character)-97)%26 )# if character is lowercase, then required modifications
            else:                   #if character is not an alphabet, append it without any change
                ciphertext+= character
        params ={'encrypted_text': ciphertext}
    return render(request,'index.html', params) 

 

#function to decrypt the message
def decrypt(request):
    ciphertext = request.GET.get('text', 'default')
    plaintext = '' #the plaintext to be returned, inititally assigned to an empty string
    if(len(ciphertext)):
        for cipher_character in ciphertext: 
            if (cipher_character.isupper()) :
                plaintext+=chr(90-(ord(cipher_character)-65)%26 )#if character is uppercase, then modify the sum
            elif cipher_character == " ":#if the character is space then it is appended as it is
                plaintext+=" "
            elif (cipher_character.islower() ):# if character is lowercase, then required modifications
                plaintext+=chr(122-(ord(cipher_character)-97)%26 )
            else:               #if character is not an alphabet, append it without any change
                plaintext+= cipher_character
        params ={'decrypted_text': plaintext}
    return render(request,'index.html', params)