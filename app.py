#Importation
from guizero import App, Box, Drawing, PushButton,info
from random import choice


#Functions
def on_click_letter(letters_list,index):
    global written,input_letters
    if written==0:
        drawing.text(20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==1:
        drawing.text(120, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==2:
        drawing.text(220, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==3:
        drawing.text(320, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==4:
        drawing.text(420, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
        
        
def on_click_backspace():
    global written,input_letters
    drawing.rectangle(pos[written-1],line, pos[written], line+100,outline=True, outline_color="white")
    written-=1
    input_letters=input_letters[:-1]
    
    
def on_click_enter():
    global step
    step="".join(input_letters)
    verification(secret_word)  
    
def verification(secret):
    global step, line,written
    user_input=step
    if user_input==secret:
            for j in range(1,6):
                drawing.rectangle(pos[j-1],line, pos[j], line+100,outline=True, outline_color="white",color="green")
            k=0
            for x in range(0,401,100):
                drawing.text(x+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
            app.info("GG!","You win")
    for i in range(len(user_input)):
        if user_input[i]==secret[i]:
            drawing.rectangle(pos[i],line, pos[i+1], line+100,outline=True, outline_color="white",color="green")
            k=0
            for x in range(0,401,100):
                drawing.text(x+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
        elif user_input[i]==secret[1] or user_input[i]==secret[2] or user_input[i]==secret[3] or user_input[i]==secret[4] :     
            drawing.rectangle(pos[i],line, pos[i+1], line+100,outline=True, outline_color="white",color="yellow")
            k=0
            for x in range(0,401,100):
                drawing.text(x+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1  
    line+=100 
    step=""
    input_letters.clear()
    written=0

#Initialisation
list_words=["CHIEN"]
secret_word=choice(list_words)
letters=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
pos=[0,100,200,300,400,500]
line=0
written=0
input_letters=[]

app=App(title="Wordle",bg=(32,32,32), width=1280,height=800)

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
enter_key.bg=(96,96,96)
for i in range(10):
    azerty=PushButton(azerty_box,text=letters[i],width=10,height=2,grid=[i,1],command=on_click_letter,args=[letters,i])
    qsdfgh=PushButton(qsdfgh_box,text=letters[i+10],width=10,height=2,grid=[i,2],command=on_click_letter,args=[letters,(i+10)])
    azerty.bg=(96,96,96)
    qsdfgh.bg=(96,96,96)
for j in range(6):
    wxcvbn=PushButton(wxcvbn_box,text=letters[20+j],width=10,height=2,grid=[j,3],command=on_click_letter,args=[letters,(j+20)])
    wxcvbn.bg=(96,96,96)

backspace=PushButton(azerty_box,text="<--",width=10,height=2,grid=[10,1],command=on_click_backspace)
backspace.bg=(96,96,96)


app.display()
