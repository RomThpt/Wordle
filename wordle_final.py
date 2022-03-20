#Importation
from guizero import App, Box, Drawing, PushButton, Window, Text
from random import choice
import requests
from bs4 import BeautifulSoup
from sys import exit

#Functions

def first_window():
    global app
    ## First Window
    app=App(title="Wordle choice", bg=(32,32,32), width=1280,height=800)
    ###Boxes
    void_text_box=Box(app,width="fill",height="fill", align="top")
    text_box=Box(app, width="fill",height="fill", align="top", layout="grid")
    #text_box.bg="green"
    void_button_box=Box(app,width="fill",height="fill", align="left")
    #void_button_box.bg="white"
    display_box=Box(app, width="fill",height="fill", layout="grid", align="left")
    

    #drawing=Drawing(display_box, width="fill", height="fill")
    text = Text(text_box, text="How many letters do you want ?", align="top", color="white", width=49, height=3, bg=(60,60,60), grid=[0,0])
    text.text_size=35
    for i in range(1,5):
        button=PushButton(display_box,text=str(i+1), grid=[i-1,1], width=15,height=8, command=set_game,args=[i+1])
        button.bg=(62,62,62)
        button.text_color=(255,255,255)
        
    app.display()    
    
def set_game(index):
    global numbers_letters, window,playground_box, wxcvbn_box, qsdfgh_box, azerty_box, drawing, line, written, input_letters
    #Initialisation
    line=0
    written=0
    input_letters=[]
    # app.hide()
    window=Window(app, title="Wordle 5",bg=(32,32,32), width=1280,height=800)
    numbers_letters=index
    
    #Boxes
    playground_box=Box(window, align="top",width=500,height=500)
    wxcvbn_box=Box(window,layout="grid",align="bottom")
    qsdfgh_box=Box(window,layout="grid",align="bottom")
    azerty_box=Box(window,layout="grid",align="bottom")
        
    #Drawing
    drawing=Drawing(playground_box,width="fill",height="fill")
    secret(numbers_letters)
    playground(numbers_letters)
    keyboard()
    
def playground(width):
    """
    
    Draw a playground of width*5
    
    """
    global pos
    pos=[0,100,200,300,400,500]
    pos_y=pos
    if width==2:
        pos=[150,250,350]
    if width==3:
        pos=pos[1:5]
    if width==4:
        pos=[50,150,250,350,450]
    for i in range(5):
        for j in range(width):
            drawing.rectangle(pos[j], pos_y[i], pos[j+1], pos_y[i+1],outline=True, outline_color="white",color="black")  

def keyboard():
    """
    
    Keyboard with PushButton

    """
    letters=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
    enter_key=PushButton(window,text="<-\n    |",width=10,height=2,command=on_click_enter)
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
        
def on_click_letter(letters_list,index):
    """
    
    When you click on a button the functions know which letters it is and write it on the playground
    
    Parameters
    ----------
    letters_list : list
        list of letters to know what letters the player can press
    index : int
        to know which letter the player pressed
    
    Globals
    -------
    written, input_letters 
    to know on wich column we work and to know wich letters have been pressed
    
    """
    global written, input_letters 
    if written==0:
        drawing.text(pos[0]+20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==1:
        drawing.text(pos[1]+20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==2 and numbers_letters>=3:
        drawing.text(pos[2]+20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==3 and numbers_letters>=4:
        drawing.text(pos[3]+20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
    elif written==4 and numbers_letters>=5:
        drawing.text(pos[4]+20, line+2, text=letters_list[index],size=60,color="white")
        written+=1
        input_letters.append(letters_list[index])
           
def on_click_backspace():
    """
    
    Delete the last character and replace it on the playground by a dark rectangle

    Globals
    -------
    written: int
        to come back to the previous column.
    input_letters: list
        to delete the previous letter in the list of letters pressed.
    
    """
    global written,input_letters
    if len(input_letters)==0:
        pass
    else:
        drawing.rectangle(pos[written-1],line, pos[written], line+100,outline=True, outline_color="white")
        written-=1
        input_letters=input_letters[:-1]
    
def on_click_enter():
    """
    
    On click enter join all of the input letters to create a word
    
    Globals
    -------
    step: str
        variable of the final word of the player.

    """
    global step
    step="".join(input_letters)
    if len(step)!=numbers_letters:
        window.warn("aie", "please "+str(numbers_letters)+" letters")
        restart=window.yesno("End","Restart?")
        if restart==True:
            restart_wordle()
        else:
             app.destroy()
    else:
        verification(secret_word)  

def verification(secret): 
    """
    
    verification try if the final word (step) is equal to the secret word
    if the letters is to the right place or if it's in the word but not in the right place'

    Parameters
    ----------
    secret : str
        the secret word
    
    Globals
    -------
    step: 
        the word inputed
    line:
        the line we are
    written:
        the columns we are

    """
    global step, line, written
    user_input=step
    if user_input==secret:
            for j in range(numbers_letters):
                drawing.rectangle(pos[j],line, pos[j+1], line+100,outline=True, outline_color="white",color="green")
            k=0
            for x in range(numbers_letters):
                drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
            restart=window.yesno("GG","Restart?")
            if restart==True:
                restart_wordle()
                return 1
            else:
                app.destroy()
                exit()
    for i in range(len(user_input)):
        if user_input[i]==secret[i]:
            drawing.rectangle(pos[i],line, pos[i+1], line+100,outline=True, outline_color="white",color="green")
            k=0
            for x in range(numbers_letters):
                drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
        else:
            for j in range(0,numbers_letters):
                if user_input[i]!=secret[i]:
                    if user_input[i]==secret[j] :  
                        drawing.rectangle(pos[i],line, pos[i+1], line+100,outline=True, outline_color="white",color="yellow")
                        k=0
                        for x in range(numbers_letters):
                            drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                            k+=1  
    line+=100 
    if line==500:
        restart=window.yesno("End","Restart?")
        if restart==True:
            restart_wordle()
            return 1
        else:
            app.destroy()
            exit()
              
    step=""
    input_letters.clear()
    written=0

def clear():
    """
    
    Initialize all of the variable
    

    """
    
    global step, written, input_letters, line
    line=0
    step=""
    input_letters.clear()
    written=0

def scrap():
    global list_words
    # 2 letters
    request=requests.get('https://www.listesdemots.net/mots2lettres.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('mot2lettres.txt', 'w') as f :
        f.write(list_words[0])
    #3 letters
    request=requests.get('https://www.listesdemots.net/mots3lettres.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('mot3lettres.txt', 'w') as f :
        f.write(list_words[0])
    #4 letters
    list_words = [elt.string.strip() for elt in p]
    request=requests.get('https://www.listesdemots.net/mots4lettres.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('mot4lettres.txt', 'w') as f :
        f.write(list_words[0])
    for i in range(2,4):
        request=requests.get('https://www.listesdemots.net/mots4lettres'+'page'+str(i)+'.htm')
        content=request.content
        soup = BeautifulSoup(content,features="lxml")
        p = soup.find_all("span", {"class": "mot"})
        list_words = [elt.string.strip() for elt in p]
        with open('mot4lettres.txt', 'a') as f :
            f.write(list_words[0])
    #5letters
    list_words = [elt.string.strip() for elt in p]
    request=requests.get('https://www.listesdemots.net/mots5lettres.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('mot5lettres.txt', 'w') as f :
        f.write(list_words[0])
    for i in range(2,11):
        request=requests.get('https://www.listesdemots.net/mots5lettres'+'page'+str(i)+'.htm')
        content=request.content
        soup = BeautifulSoup(content,features="lxml")
        p = soup.find_all("span", {"class": "mot"})
        list_words = [elt.string.strip() for elt in p]
        with open('mot5lettres.txt', 'a') as f :
            f.write(list_words[0])
     
def restart_wordle():
    global secret_word
    clear()
    playground(numbers_letters)
    secret(numbers_letters)
   
def secret(width):
    global secret_word
    if width==2:
        with open('mot2lettres.txt','r') as f:
            all_words=f.read()
            list_words = all_words.split()
            secret_word = choice(list_words)
            print(secret_word)
    if width==3:
        with open('mot3lettres.txt','r') as f:
            all_words=f.read()
            list_words = all_words.split()
            secret_word = choice(list_words)
            print(secret_word)
    if width==4:
        with open('mot4lettres.txt','r') as f:
            all_words=f.read()
            list_words = all_words.split()
            secret_word = choice(list_words)
            print(secret_word)
    if width==5:
        with open('mot5lettres.txt','r') as f:
            all_words=f.read()
            list_words = all_words.split()
            secret_word = choice(list_words)
            print(secret_word)

# My giga slave
first_window()
