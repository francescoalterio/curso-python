import json
import random

def get_word():
    with open('palabras.json') as words_json:
        words = json.load(words_json)
        return words[random.randint(0, len(words) - 1)]
        
def verify_word(word, user_word):
    tries = []
    word_count = {}
    user_word_count = {}
    for letter in word:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1

        user_word_count[letter] = 0
    for index, letter in enumerate(word):
        if letter == user_word[index]:
            tries.append("c")
            if letter in user_word_count:
                user_word_count[letter] += 1
            else:
                user_word_count[letter] = 1
        else:
            tries.append(" ")
    
    for index, letter in enumerate(user_word):
        if letter != word[index] and letter in word:
            if user_word_count[letter] < word_count[letter]:
                tries[index] = "x"
                user_word_count[letter] += 1

    
    return tries



def main():
    while True:
        word = get_word()
        print(word)
        while True:
            word_intent = input(f"Ingrese una palabra de {len(word)} caracteres: ")
            if len(word_intent) != len(word):
                print(f' La palabra a adivinar tiene {len(word)} - "{word_intent}" tiene {len(word_intent)}')
                continue
            word_virified = verify_word(word, word_intent)
            print("* - - - - - *")
            print(f'| {" ".join(word_intent).upper()} |')
            print("* - - - - - *")
            print(f'| {" ".join(word_virified)} |')
            print("* - - - - - *")
            if word_virified.count("c") == len(word):
                print("VICTORIAAA!!")
                break
            


        salir = input("Desea salir del juego? (s/n)")
        if (salir.lower() == "s"):
            break
main()