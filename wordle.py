from random import choice
from jeu import Game

def separation(word):
    list_letters=[]
    for letter in word:
        list_letters.append(letter)
    return list_letters


def verification(word,chances):
    user_input=input("Devine : ").upper()
    assert len(user_input)==5,"Entrez 5 lettres"
    if user_input==word:
        print("gg")
        return False
    for i in range(len(user_input)):
        if user_input[i]==word[i]:
            print("bonne place")
        elif user_input[i]==word[1] or user_input[i]==word[2] or user_input[i]==word[3] or user_input[i]==word[4] :     
            print("lettre existante")  
        else:
            print("perdu")
    chances-=1
    return chances


def game():
    #CAPS ONLY
    list_words=["CHIEN", "CHATE", "LOUVE"]
    game_active=True
    player_chances=4
    secret_word=choice(list_words)
    # secret_letters=separation(secret_word)
    while game_active:
        if player_chances<=0:
            break
        if verification(secret_word,player_chances)==False:
            break
        else:
            player_chances=verification(secret_word, player_chances)
            print(player_chances)
        
game()