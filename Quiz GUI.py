from tkinter import *
import random
from tkinter import messagebox

question=[
    "Which one of the following has maximum number of atoms?",
    "Survival of plants in terrestrial environment has been made possible by the presence of",
    "In which group of animals coelom is filled with blood?",
    "Organisms without nucleus and cell organelles belong to",
    "Which cells do not have perforated cell walls?",
    "The numerical ratio of displacement to distance covered by a moving object is",
    "According to the third law of motion, action and reaction",
    "The value of acceleration due to gravity",
    "The gravitational force between two objects is F. If the masses of both objects are halved without changing distance between them, then the gravitational force would become",
    "Among the given options, which one is not correct for the use of large amount of fertilisers and pesticides?",
]

answers_choice=[
    ["(a) 18 g of H2O","(b) 18 g of O2","(c) 18 g of CO2","(d) 18 g of CH4",],
    ["(a) intercalary meristem","(b) conducting tissue","(c) apical meristem","(d) parenchymatous tissue"],
    ["(a) Arthropoda","(b) Annelida","(c) Nematoda","(d) Echinodermata"],
    ["(a) fungi","(b) protista","(c) algae","(d) bacteria",],
    ["(a) Tracheids","(b) Companion cells","(c) Sieve tubes","(d) Vessels",],
    ["(a) always less than 1","(b) always equal to 1","(c) always more than 1","(d) equal or less than 1",],
    ["(a) always act on the same body","(b) always act on different bodies in opposite directions","(c) have same magnitude and direction","(d) act on either body at normal to each other",],
    ["(a) is least on equator","(b) is least on poles","(c) is same on equator and poles","(d) increases from pole to equator",],
    ["(a)F/4", "(b)F/2","(c)F" , "(d)2F",],
    ["(a) They are eco-friendly","(b) They turn the fields barren after some time","(c) They remove the useful component from the soil","(d) They destroy the soil fertility",],
]

answer=[1,1,0,0,1,1,2,3,1,2]
user_answer=[]

indexes=[]
def gen():
    global indexes
    while(len(indexes)<10):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)

def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background="#ffffff"

    )
    labelimage.pack(pady=(50,40))
    labelresulttext=Label(
        root,
        font=("Consolas",20),
        background="#ffffff"
    )
    labelresulttext.pack()
    if score >=80:
        img=PhotoImage(file="greatjob.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You are doing great.!!!")
        labelresulttext.configure(text=score)
    elif(score<=50 and score>30):
        img=PhotoImage(file="itsok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You are doing ok man.!!!")
        labelresulttext.configure(text=score)
    else:
        img=PhotoImage(file="workhard.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You should work harder man.!!!")
        labelresulttext.configure(text=score)

def calc():
    global indexes,user_answer,answer
    x=0
    score=0
    for i in indexes:
        if user_answer[x] == answer[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)

ques=1

def selected():
    global radiovar,user_answer
    global lblquestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques <10:
        lblquestion.config(text=question[indexes[ques]])
        r1['text']=answers_choice[indexes[ques]][0]
        r2['text']=answers_choice[indexes[ques]][1]
        r3['text']=answers_choice[indexes[ques]][2]
        r4['text']=answers_choice[indexes[ques]][3]
        ques+=1
    else:
        calc()



def startquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion=Label(
        root,
        text=question[indexes[0]],
        font=("Consolas",16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"
    )
    lblquestion.pack(pady=(150,20))

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times",12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r1.pack(pady=5)


    r2=Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times",12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=5)


    r3=Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times",12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r3.pack(pady=5)


    r4=Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times",12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=5)



def startispressed():
    logoimage.destroy()
    labeltext.destroy()
    lblinstruction.destroy()
    lblrules.destroy()
    btnstart.destroy()
    gen()
    startquiz()

root=Tk()
root.title("LearnVern Quiz")
root.geometry('700x600')
root.resizable(False,False)
root.config(background='#FFFFFF')

def aboutus():
    msg=messagebox.showinfo("About The Developer","Hii, my name is Ayush\nI am the developer of this software\nVisit www.finitecoding.com for more info")




menubar=Menu(root)
aboutmenu=Menu(menubar,tearoff=0)
aboutmenu.add_command(label="Know About Us",background="#ffffff",command=aboutus)
aboutmenu.add_separator()

aboutmenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label='About Us',menu=aboutmenu)
root.config(menu=menubar)
logo = PhotoImage(file="tiktok.png")

logoimage=Label(
    root,
    image=logo,
    background='#FFFFFF',
)
logoimage.pack()

labeltext=Label(
    root,
    text='LearnVern Quiz',
    font = ("Comic sans MS",24,'bold'),
    background='#FFFFFF',
)
labeltext.pack(pady=(0,20))

startimage=PhotoImage(file='startquiz.png')
btnstart=Button(
    root,
    image=startimage,
    background='#ffffff',
    relief=FLAT,
    bd=0,
    command=startispressed,

)
btnstart.pack()

lblinstruction=Label(
    root,
    text="Welcome to our quiz portal\nPlease go through the instruction given below\nAfter that you can start the quiz.",
    font=('Helvetics',12),
    background='#ffffff'
)
lblinstruction.pack(pady=(0,120))

lblrules=Label(
    root,
    text='There will be 10 questions in the quiz\nYou will only get a limited second for answering each question\nThe option that will be ticked first will be submission choice',
    width=100,
    font=('Times',14)
)
lblrules.pack()
root.mainloop()