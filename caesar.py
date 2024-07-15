##Caesar Cipher Python project by Halil Furkan Karademir
##Don't forget the star project if you liked the project :)

from termcolor import colored


capital_letters = (
    [chr(codepoint) for codepoint in range(0x0041, 0x005A + 1)]   # Latin (English, Spanish, French, German, Portuguese)
    
)
small_letters = (
    [chr(codepoint) for codepoint in range(0x0061, 0x007A + 1)]   # Latin (English, Spanish, French, German, Portuguese)
     # Bengali
)

def main():
    while True:
        option = input("Choose your option\n1.Encode\n2.Decode with key\n3.Decode without key\n4.Exit\n")
        if option == "1":
            caesar_cipher_encoder()
        elif option == "2":
            caesar_cipher_decoder()
        elif option == "3":
            caesar_cipher_decoder_no_key()    
        elif option == "4":
            thanks_message = colored("Thanks for using this app :)",'green',attrs=['bold'])
            print(thanks_message)
            break
        else:
            error_message = colored("Invalid option. Please choose again.",'red',attrs=['bold'])
            print(error_message)

def caesar_cipher_encoder():
    input_text = input("Write the text to be encoded:")
    shift_key = int(input("Write key index:"))
    encoded_text = ""
    is_invalid = False
    for i in range(len(input_text)):
        for j in range(0, 26):
            new_index = (j + shift_key) % 26
            if input_text[i] == capital_letters[j]:
                encoded_text += capital_letters[new_index]
            elif input_text[i] == small_letters[j]:
                encoded_text += small_letters[new_index]
            
            
        if input_text[i] == " " or not is_letter_in_lists(input_text[i]):
            encoded_text += input_text[i]
    colored_text = colored(encoded_text, 'cyan', attrs=['bold'])    
    if not is_invalid:
        print("\n\nEncoded text:", colored_text, "\n\n")

def caesar_cipher_decoder():
    input_text = input("Text to decode:")
    shift_key = int(input("Key index:"))
    shift_key = -shift_key
    decoded_text = ""
    for i in range(len(input_text)):
        for j in range(0, 26):
            new_index = (j + shift_key) % 26
            if input_text[i] == capital_letters[j]:
                decoded_text += capital_letters[new_index]
            elif input_text[i] == small_letters[j]:
                decoded_text += small_letters[new_index]
        if input_text[i] == " " or not is_letter_in_lists(input_text[i]):
            decoded_text += input_text[i]
    colored_text = colored(decoded_text, 'cyan', attrs=['bold'])
    print("\n\nDecoded text:", colored_text, "\n\n")

def caesar_cipher_decoder_no_key():
    input_text = input("Text to decode:")
    for shift_key in range(26):
        decoded_text = ""
        for char in input_text:
            if char in capital_letters:
                original_index = capital_letters.index(char)
                new_index = (original_index - shift_key) % 26
                decoded_text += capital_letters[new_index]
            elif char in small_letters:
                original_index = small_letters.index(char)
                new_index = (original_index - shift_key) % 26
                decoded_text += small_letters[new_index]
            elif char == " ": 
                decoded_text += " "
          
        colored_text = colored(decoded_text, 'cyan', attrs=['bold']) 
        print("%d.decoded text is: %s\n" % (shift_key + 1, colored_text)) 

def is_letter_in_lists(char):
    
    return char in capital_letters or char in small_letters

if __name__ == "__main__":
    main()
