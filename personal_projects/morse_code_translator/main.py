

import pygame
import time


pygame.mixer.init()


short_sound = pygame.mixer.Sound("short_morse.wav")
long_sound = pygame.mixer.Sound("long_morse.wav")


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def convert_text(text):
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += "?"
    return morse_code


def play_audio(morse_code):
    for char in morse_code:
        if char == ".":
            short_sound.play()
            time.sleep(short_sound.get_length())
        elif char == "-":
            long_sound.play()
            time.sleep(short_sound.get_length())
        elif char == "/":
            time.sleep(short_sound.get_length())
        else:
            time.sleep(short_sound.get_length())
        time.sleep(short_sound.get_length())


def main():

    input_text = input(
        "What would you like translated into morse code?: ").upper()
    morse_code = convert_text(input_text)
    print(morse_code)
    play_audio(morse_code)


if __name__ == "__main__":
    main()


