#Importation
from guizero import App, Box, Drawing, PushButton,info
from random import choice


#Functions
def on_click_letter(letters_list,index):
    global written,input_letters
    if written==0:
        drawing.text(20, 2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        print(input_letters)
    elif written==1:
        drawing.text(120, 2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        print(input_letters)
    elif written==2:
        drawing.text(220, 2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        print(input_letters)
    elif written==3:
        drawing.text(320, 2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        print(input_letters)
    elif written==4:
        drawing.text(420, 2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        print(input_letters)
        
        
def on_click_backspace():
    global written,input_letters
    drawing.rectangle(pos[written-1],0, pos[written], 100,outline=True, outline_color="white")
    written-=1
    input_letters=input_letters[:-1]
    print(input_letters)
    
    
def on_click_enter():
    global step
    step="".join(input_letters)
    verification(secret_word)
        
def verification(secret):
    user_input=step
    if user_input==secret:
            for j in range(1,6):
                drawing.rectangle(pos[j-1],0, pos[j], 100,outline=True, outline_color="white",color="green")
            i=0
            for x in range(0,401,100):
                drawing.text(x+20, 2, text=input_letters[i],size=60,color="white")
                i+=1
            app.info("GG!","You win")
    for i in range(len(user_input)):
        if user_input[i]==secret[i]:
            print("bonne place")
        elif user_input[i]==secret[1] or user_input[i]==secret[2] or user_input[i]==secret[3] or user_input[i]==secret[4] :     
            print("lettre existante")  
        else:
            print("perdu")

"""
def game():
    #CAPS ONLY
    
    game_active=True
    player_chances=4
    
    # secret_letters=separation(secret_word)
    while game_active:
        if player_chances<=0:
            break
        if verification(secret_word,player_chances)==False:
            break
        else:
            player_chances=verification(secret_word, player_chances)
     """   

#Initialisation
list_words=["CHIEN"]
secret_word=choice(list_words)
letters=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
pos=[0,100,200,300,400,500]
written=0
input_letters=[]

app=App(title="Wordle",bg="grey", width=1280,height=800)

#Boxes
playground_box=Box(app, align="top",border=True,width=500,height=500)
wxcvbn_box=Box(app,layout="grid",align="bottom")
qsdfgh_box=Box(app,layout="grid",align="bottom")
azerty_box=Box(app,layout="grid",align="bottom")


drawing=Drawing(playground_box,width="fill",height="fill")
drawing.bg="white"


#Playground
for i in range(1,6):
    for j in range(1,6):
        drawing.rectangle(pos[j-1], pos[i-1], pos[j], pos[i],outline=True, outline_color="white")


#Keybord
enter_key=PushButton(app,text="<-\n    |",width=10,height=2,command=on_click_enter)
for i in range(10):
    actual_letter=PushButton(azerty_box,text=letters[i],width=10,height=2,grid=[i,1],command=on_click_letter,args=[letters,i])
    actual_letter=PushButton(qsdfgh_box,text=letters[i+10],width=10,height=2,grid=[i,2],command=on_click_letter,args=[letters,(i+10)])
for j in range(6):
    actual_letter=PushButton(wxcvbn_box,text=letters[20+j],width=10,height=2,grid=[j,3],command=on_click_letter,args=[letters,(j+20)])

backspace=PushButton(azerty_box,text="<--",width=10,height=2,grid=[10,1],command=on_click_backspace)

app.display()
