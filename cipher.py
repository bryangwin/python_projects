logo = '''

    _______\\__
   (_. _ ._  _/
    '-' \__. /
         /  /
        /  /    .--.  .--.
       (  (    / '' \/ '' \   "
        \  \_.'            \   )
        ||               _  './
         |\   \     ___.'\  /
           '-./   .'    \ |/
              \| /       )|
               |/       // \\
               |\    __//   \\__
              //\\  /__/     \__|
          .--_/  \_--.
         /__/      \__

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

keep_going = True

while keep_going:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
  
    def cipher_magic(text, shift, direction):
        final_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter not in alphabet:
                final_text += letter
            else:
                position = alphabet.index(letter)
                letter = alphabet[position + shift]
                final_text += letter
        print(f"The {direction}d text is: {final_text}")

    cipher_magic(text, shift, direction)
    continue_question = input("Would you like to use this service again? Type 'y' or 'n': ")
    
    if continue_question == "n":
        keep_going = False
        print("Goodbye.")
    elif continue_question != "y" and continue_question != "n":
        print("That is not a valid response. We will keep going to be safe.")
    

