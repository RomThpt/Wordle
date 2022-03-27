#Importation
from guizero import App, Box, PushButton, Drawing, Window, Text, Picture, Slider
from random import choice
import requests
from bs4 import BeautifulSoup
from sys import exit
import unidecode

#Functions
def closing():
    """
    Function that close all of the windows ( fix bug)

    Returns
    -------
    int
        Return 1 if the player want to quit to fix a bug.

    """
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        exit()
        return 1
        
def first_window():
    """
    It's the first window that appears, in others words, App
    It initializes all of the color, all of the boxes, and interactions like buttons or text

    Returns
    -------
    None.
    
    Globals
    -------
    app:
        the app window, this way, all of the other function can have access to the app
    pokemon_active:
        We want to know if the player choose the classic game mode or the pokemon game mode
    bg_color:
        the background color to change it when the user want
    text:
        We want to change the color of the text if the player want
    button_color:
        We want to chnage the color of the buttons and the interrraction when the player want
    display_box:
        the other functions can modify the display_box 

    """
    global app, pokemon_active, bg_color,text, button_color, display_box
    pokemon_active=False
    bg_color=(32,32,32)
    button_color=(62,62,62)
    ## First Window
    app=App(title="Wordle choice", bg=bg_color, width=1280,height=800)
    ###Boxes
    settings_box=Box(app,width="fill",height=45, align="top")
    settings=Picture(settings_box, image="settings.png", align="right", width=45, height=45)
    settings.when_clicked=parameter
    Box(app,width="fill",height="fill", align="top")
    text_box=Box(app, width="fill",height="fill", align="top", layout="grid")
    Box(app,width="fill",height="fill", align="left")
    display_box=Box(app, width="fill",height="fill", layout="grid", align="left")
    
    text = Text(text_box, text="How many letters do you want ?", align="top", color="white", width=49, height=3, bg=button_color, grid=[0,0])
    text.text_size=35
    for i in range(1,5):
        button=PushButton(display_box,text=str(i+1), grid=[i-1,1], width=20,height=15, command=set_game,args=[i+1])
        button.bg=button_color
        button.text_color=(255,255,255)
    pokemon_box=Box(app,width=20,height=12, align="bottom")
    pokemon_picture = Picture(pokemon_box, image="pokemon.png", align="right", width=22, height=12)
    pokemon_picture.when_clicked = pokemon_first_window
    app.when_closed=closing
    app.display()

def parameter():
    """
    The fuction that create a parameter_window that used to change the color of the background and interrractions

    Returns
    -------
    None.

    """
    def come_back():
        """
        Used to came back on the app window
        
        """
        settings_window.destroy()
        
    def bg_color_changing(white_coefficient):
        """
        The function for the slider 
        like that we know wich color the user want

        Parameters
        ----------
        white_coefficient : str
            The value of the slider.

        Globals
        -------
        bg_color:
            like that the the value of the button color is free and we can use it to change the bg color
        button_color:
            like that we can change interractions color and buton color
        text_rgb:
            like that we can chnage the text color
        
        """
        global bg_color,button_color, text_rgb
        bg_color=(int(white_coefficient), int(white_coefficient), int(white_coefficient))
        button_color=(255-bg_color[0]-30,255-bg_color[1]-30,255-bg_color[2]-30)
        if int(white_coefficient)<=120:
            text_rgb=(0,0,0)
        else:
            text_rgb=(255,255,255)
            
    def confirm_bg():
        """
        It's the function of the button that confirm what kind of color do the user want

        """
        settings_window.bg=bg_color
        app.bg=bg_color
        app.text_color=text_rgb
        for i in range(1,5):
            button=PushButton(display_box,text=str(i+1), grid=[i-1,1], width=20,height=15, command=set_game,args=[i+1])
            button.bg=button_color
        text.bg=button_color
        settings_window.text_color=text_rgb
        slider.bg=button_color
        confirm_button.bg=button_color
        dark_mode.bg=button_color

    def dark_mode_setup():
        """
        The function of the button that set the main color, in others words to the dark mode color

        """
        global bg_color, button_color
        bg_color=(32,32,32)
        button_color=(62,62,62)
        text_rgb="white"
        app.bg=bg_color
        app.text_color=text_rgb
        for i in range(1,5):
            button=PushButton(display_box,text=str(i+1), grid=[i-1,1], width=20,height=15, command=set_game,args=[i+1])
            button.bg=button_color
        text.bg=button_color
        settings_window.text_color=text_rgb
        slider.bg=button_color
        confirm_button.bg=button_color
        dark_mode.bg=button_color

    settings_window=Window(app, title="Settings",bg=bg_color, width=350,height=500)
    settings_window.when_closed=come_back
    slider=Slider(settings_window,32,200,command=bg_color_changing)
    slider.bg=button_color
    confirm_button=PushButton(settings_window,text="Confirm?", width=30,height=5, command=confirm_bg)
    confirm_button.bg=button_color
    dark_mode=PushButton(settings_window,text="Dark mode?", width=30,height=5, command=dark_mode_setup)
    dark_mode.bg=button_color

def set_game(len_want):
    """
    The game_window with all of the game tools like keyboard, the playground and so on

    Parameters
    ----------
    len_want : int
        The length that the user want to deals with.

    Returns
    -------
    None.
    
    Globals
    -------
    length_letters:
        It's the length of the word the user want
    game_window:
        like that the other function can modify the game window for exemple the keyboard
    playground_box, wxcvbn_box, qsdfgh_box, azerty_box:
        like that the other functions can modify boxes
    drawing:
        like that other functions can draw
    line:
        to know on wich line we are (how many chances left)
    written:
        how many letters are inputed (on wich column)
    input_letters:
        wich letters are inputed
    
    """
    global length_letters, game_window, playground_box, wxcvbn_box, drawing, qsdfgh_box, azerty_box, line, written, input_letters
    
    def come_back():
        """
        the function to go on the other game_mode
        
        """
        game_window.destroy()
        if pokemon_active:
            pokemon_window.show()
        else:
            app.show()
            
    #Initialisation
    line=0
    written=0
    input_letters=[]
    app.hide()
    game_window=Window(app, title="Wordle",bg=bg_color, width=1280,height=800)
    game_window.when_closed=come_back
    length_letters=len_want#len of the word
    
    #Boxes
    playground_box=Box(game_window, align="top",width=500,height=500)
    wxcvbn_box=Box(game_window,layout="grid",align="bottom")
    qsdfgh_box=Box(game_window,layout="grid",align="bottom")
    azerty_box=Box(game_window,layout="grid",align="bottom")
        
    drawing=Drawing(playground_box,width="fill",height="fill")
    
    secret(length_letters)
    playground(length_letters)
    keyboard()
    
def playground(width):
    """
    
    Setup and draw a playground of width*5 depending of the length desired
    
    Globals
    -------
    pos:
        the position of cubes depending of the length desired
    playground_box:
        like that other function can modify this box
    
    """
    def draw_playground():
        """
        Draw a playground of width*5 depending of the length desired

        """
        for i in range(5):
            for j in range(width):
                drawing.rectangle(pos[j], pos_y[i], pos[j+1], pos_y[i+1],outline=True, outline_color="white",color="black") 
                
    global pos,playground_box
    pos=[0,100,200,300,400,500]
    pos_y=pos
    if pokemon_active:
        for x in range(6,13):
            if width==x:
                playground_box.width=x*100
                pos.append(x*100)
                break
            pos.append(x*100)
        draw_playground()  
    if width==2:
        pos=[150,250,350]
    if width==3:
        pos=pos[1:5]
    if width==4:
        pos=[50,150,250,350,450]
    draw_playground()      

def keyboard():
    """
    
    Keyboard with PushButton

    """
    letters=["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","-"]
    enter_key=PushButton(game_window,text="<-\n    |",width=10,height=2,command=on_click_enter)
    enter_key.bg=(96,96,96)
    for i in range(10):
        azerty=PushButton(azerty_box,text=letters[i],width=10,height=2,grid=[i,1],command=on_click_letter,args=[letters,i])
        qsdfgh=PushButton(qsdfgh_box,text=letters[i+10],width=10,height=2,grid=[i,2],command=on_click_letter,args=[letters,(i+10)])
        azerty.bg=(96,96,96)
        qsdfgh.bg=(96,96,96)
    for j in range(7):
        wxcvbn=PushButton(wxcvbn_box,text=letters[20+j],width=10,height=2,grid=[j,3],command=on_click_letter,args=[letters,(j+20)])
        wxcvbn.bg=(96,96,96)
    
    backspace=PushButton(azerty_box,text="<--",width=10,height=2,grid=[10,1],command=on_click_backspace)
    backspace.bg=(96,96,96)
        
def on_click_letter(letters_list,index_letter):
    """
    
    When you click on a button the functions know which letters it is and write it on the playground
    
    Parameters
    ----------
    letters_list : list
        list of letters to know what letters the player can press
    index_letter : int
        to know which letter the player pressed
    
    Globals
    -------
    written, input_letters 
    to know on wich column we work and to know wich letters have been pressed
    
    """
    global written, input_letters 
    for i in range(13):
        if written==i and length_letters>=i+1:
            if letters_list[index_letter]=="I" or letters_list[index_letter]=="-":
                drawing.text(pos[i]+35, line+2, text=letters_list[index_letter],size=60,color="white")
                written+=1
                input_letters.append(letters_list[index_letter])
                break
            else:
                drawing.text(pos[i]+20, line+2, text=letters_list[index_letter],size=60,color="white")
                written+=1
                input_letters.append(letters_list[index_letter])
                break
           
def on_click_backspace():
    """
    Delete the last character and replace it on the playground with a dark rectangle

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
    if len(step)!=length_letters:
        game_window.warn("aie", "please "+str(length_letters)+" letters")
        restart=game_window.yesno("End","Restart?")
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
            for j in range(length_letters):
                drawing.rectangle(pos[j],line, pos[j+1], line+100,outline=True, outline_color="white",color="green")
            k=0
            for x in range(length_letters):
                drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
            restart=game_window.yesno("GG","Restart?")
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
            for x in range(length_letters):
                drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                k+=1
        else:
            for j in range(0,length_letters):
                if user_input[i]!=secret[i]:
                    if user_input[i]==secret[j] :  
                        drawing.rectangle(pos[i],line, pos[i+1], line+100,outline=True, outline_color="white",color="yellow")
                        k=0
                        for x in range(length_letters):
                            drawing.text(pos[x]+20, line+2, text=input_letters[k],size=60,color="white")
                            k+=1  
    line+=100 
    if line==500:
        restart=game_window.yesno("End","Restart?")
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
    
    Globals
    -------
    step, written, input_letters, line:
        initialize all of this variable
    """
    
    global step, written, input_letters, line
    line=0
    step=""
    input_letters.clear()
    written=0

def scrap():
    """
    Scraping method

    """
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
    #21 letters
    request=requests.get('https://www.listesdemots.net/mots21lettres.htm')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    p = soup.find_all("span", {"class": "mot"})
    list_words = [elt.string.strip() for elt in p]
    with open('mot21lettres.txt', 'w') as f :
        f.write(list_words[0])
    #Pokemon
    list_words=[]
    request=requests.get('https://www.pokemontrash.com/pokedex/liste-pokemon.php')
    content=request.content
    soup = BeautifulSoup(content,features="lxml")
    a = soup.find_all("a", {"class" :"name" })
    list_words = [elt.string.strip() for elt in a]
    tri_pokemon_letters()
         
def restart_wordle():
    """
    Restart the game

    """
    global secret_word
    clear()
    playground(length_letters)
    secret(length_letters)
   
def secret(width):
    """
    Create the secret value randomly
    
    Parameters
    ----------
    width : int
        length that the user want to deals with.
        
    Globals
    -------
    secret_word:
        the secret word
    """
    global secret_word
    for i in range(2,6):
        if width==i:
            with open('mot'+str(i)+'lettres.txt','r') as f:
                all_words=f.read()
                list_words = all_words.split()
                secret_word = choice(list_words)
                print(secret_word)
    if width==21:
        with open('mot21lettres.txt','r') as f:
            all_words=f.read()
            list_words = all_words.split()
            secret_word = choice(list_words)
            print(secret_word)
    if pokemon_active:
        for i in range(4,13):
            if width==i:
                with open('pokemon_'+str(i)+'.txt','r') as f:
                    all_words=f.read()
                    list_words = all_words.split()
                    secret_word = choice(list_words)
                    print(secret_word)
        
def tri_pokemon_letters():
    """
    Function that sort pokemon's names by their length

    """
    for i in range(4,13):
        with open('pokemon_'+str(i)+'.txt', 'w',encoding="utf-8") as f :
                    f.write("")
        for pokemon in list_words:
            if len(pokemon)==i:
                with open('pokemon_'+str(i)+'.txt', 'a',encoding="utf-8") as f :
                    f.write(unidecode.unidecode(pokemon).upper()+" ")

def pokemon_first_window():
    """
    The window to play at the pokmon Wordle

    Globals
    -------
    pokemon_window:
        like thta the other function can modify the pokemon window
    pokmon_active:
        to initialize the game mode

    """
    global pokemon_window, pokemon_active
    def come_back():
        """
        To come back on the classic page
        
        """
        app.show()
        pokemon_window.destroy()
        
    app.hide()
    pokemon_active=True
    # First Pokemon Window
    pokemon_window=Window(app,title="Wordle choice", bg=bg_color, width=1280,height=800)
    pokemon_window.when_closed=closing
    #Picture
    Picture(pokemon_window, image="pokemon.png", align="top", width=1000, height=350)
    #Form
    Box(pokemon_window,width="fill",height="fill", align="top")
    text_box=Box(pokemon_window, width="fill",height="fill", align="top", layout="grid")
    Box(pokemon_window,width="fill",height="fill", align="left")
    display_box=Box(pokemon_window, width="fill",height="fill", layout="grid", align="left")
    #Text
    text = Text(text_box, text="How many letters do you want ?", align="top", color="white", width=49, height=3, bg=(60,60,60), grid=[0,0])
    text.text_size=35
    #Button
    for i in range(4,13):
        button=PushButton(display_box,text=str(i), grid=[i,1], width=5,height=5, command=set_game,args=[i])
        button.bg=(62,62,62)
        button.text_color=(255,255,255)
    #Secret
    worlde_box=Box(pokemon_window,width=20,height=12, align="bottom")
    worlde_picture = Picture(worlde_box, image="wordle_image.png", align="right", width=15, height=15)
    worlde_picture.when_clicked=come_back

# My giga slave
first_window()
if closing()==1:
    exit()
