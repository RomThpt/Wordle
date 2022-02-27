from random import choice

class Game():
    def __init__(self):
        self.list_words=["CHIEN", "CHATE", "LOUVE"]
        self.game_active=True
        self.player_chances=4
        self.secret_word=choice(self.list_words)

        while self.game_active:
            if self.player_chances<=0:
                break
            if verification(self.secret_word,self.player_chances)==False:
                break
            else:
                player_chances=verification(self.secret_word, player_chances)
                print(player_chances)

    def verification(self,word,chances):
        self.user_input=input("Devine : ").upper()
        assert len(self.user_input)==5,"Entrez 5 lettres"
        if self.user_input==word:
            print("gg")
            return False
        for i in range(len(self.user_input)):
            if self.user_input[i]==word[i]:
                print("bonne place")
            elif self.user_input[i]==word[1] or self.user_input[i]==word[2] or self.user_input[i]==word[3] or self.user_input[i]==word[4] :     
                print("lettre existante")  
            else:
                print("perdu")
        chances-=1
        return chances

    
game=Game()