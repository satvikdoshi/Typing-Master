# tkinter is the module that's help us to create GUI, it has lots of methods and classes, which help us to easily create the gui.

from operator import le
import threading  # For threading concept
from os import stat  # For os related tasks
import random # To generate the random choice and numbers
import ttkthemes # for themes
from tkinter import * # To design the GUI
from tkinter import font # For font purpose
from tkinter import ttk  # To apply themes on components
from time import sleep   # For time purpose

# Fucntionality part
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0

# def open_popup():
#    top= Toplevel(root)
#    top.resizable(0,0)
#    top.geometry("300x300+250+100")
#    top.title("Time UP!")
#    Label(top, text= "Time UP!", font=('Arial', 18 ,'bold')).place(x=150,y=80)

def start_timer(): 
    """Starting the Timer"""
    start_button.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus() # Auto-cursor gets focus

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time 
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update() # Updating the Frame for let'us result.
    # open_popup()
    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)


def count(): 
    """Checks the Functionality like Matching of Words, Elsapsed time and WPM"""
    global wrongwords
    # global elapsedtimeinminutes
    while time!=totaltime:
        enteredpara=textarea.get(1.0,END).split()
        totalwords=len(enteredpara)
    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split() # getting value of the 'text' key in textarea

    for pair in list(zip(para_word_list,enteredpara)): # zip the both and returns the tuple 
        if pair[0]!=pair[1]:
            wrongwords+=1
    wrongwords_count_label.config(text=wrongwords)

    
    elapsedtimeinminutes=time/60  # getting time in minutes
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes  # getting words per minutes 
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100 
    accuracy=round(accuracy)                  
    accuracy_percentage_label.config(text=str(accuracy)+ '%')

def start(): 
    # Providing thread to start_timer function
    t1=threading.Thread(target=start_timer)
    t1.start()

    # Providing thread to count function
    t2=threading.Thread(target=count)
    t2.start()

def reset(): 
    """Reseting all components as fresh"""
    global time,elapsedtimeinminutes
    time=0 
    elapsedtimeinminutes=0

    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percentage_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')




# GUI Part
root= ttkthemes.ThemedTk()  # Tk is the class (themed tk class)
root.get_themes() # getting theme
root.set_theme('radiance') # setting theme
root.geometry('950x735+200+10') # applying width and height
root.resizable(0,0) # cant' change width and height
root.overrideredirect(True) # removes the title bar

# MainFrame
mainframe=Frame(root,bd=4)
mainframe.grid() #row,cols=0,0

# TitleFrame
titleFrame=Frame(mainframe,bg='orange')
titleFrame.grid() #row,cols=0,0
titleLabel=Label(titleFrame,text="TYPING MASTER",font=('algerian',28,'bold'),bg='goldenrod3',fg="white",width=38,bd=10)
titleLabel.grid(pady=5) # padding at y 

# ParagraphFrame
paragraph_frame=Frame(mainframe)
paragraph_frame.grid(rows=1,column=0) 


paragraph_list=[
"Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and",
 "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be  ",
 "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover  " ,
 "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to"]

random.shuffle(paragraph_list) # Directly changes inside list.


label_paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'))
label_paragraph.grid(row=0,column=0)

# TextAreaFrame
textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea=Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid(row=0,column=0)

# FrameOutput (Includes All Texts)
frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

# Elasped-Time-Label
elapsed_time_label=Label(frame_output,text="Elapsed Time",font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0)

# Elsaped-Timer-Label
elapsed_timer_label=Label(frame_output,text="0",font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

# Remaining-Time-Label
remaining_time_label=Label(frame_output,text="Remaining Time",font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

# Remaining-Timer-Label
remaining_timer_label=Label(frame_output,text="60",font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

# WPM-label
wpm_label=Label(frame_output,text="WPM",font=('Tahoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)

# WPM-Count-Label
wpm_count_label=Label(frame_output,text="0",font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

# Total-Words-Label
totalwords_label=Label(frame_output,text="Total Words",font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=6,padx=5)

# Total-Words-Count-Label
totalwords_count_label=Label(frame_output,text="0",font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=7,padx=5)

# WrongWords-Label
wrongwords_label=Label(frame_output,text="Wrong Words",font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=8)

# WrongWords-Count-Label
wrongwords_count_label=Label(frame_output,text="0",font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=9,padx=5)

# Accuracy-Label
accuracy_label=Label(frame_output,text="Accuracy",font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

# Accuracy-Percentage-Label
accuracy_percentage_label=Label(frame_output,text="0",font=('Tahoma',12,'bold'))
accuracy_percentage_label.grid(row=0,column=11,padx=5)

# ButtonFrame
buttons_frame=Frame(mainframe)
buttons_frame.grid(row=4,column=0)

# StartButton
start_button=ttk.Button(buttons_frame,text="Start",command=start)
start_button.grid(row=0,column=0,padx=10)

# ResetButton
reset_button=ttk.Button(buttons_frame,text="Reset",state=DISABLED,command=reset)
reset_button.grid(row=0,column=1,padx=10)

# ExitButton
exit_button=ttk.Button(buttons_frame,text="Exit",command=root.destroy)
exit_button.grid(row=0,column=2,padx=10)

# KeyboardFrame
keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

# Frame1To0
frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0)

# Label1
label1=Label(frame1to0,text="1",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label1.grid(row=0,column=0,padx=5)

# Label2
label2=Label(frame1to0,text="2",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2.grid(row=0,column=1,padx=5)

# Label3
label3=Label(frame1to0,text="3",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3.grid(row=0,column=2,padx=5)

# Label4
label4=Label(frame1to0,text="4",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4.grid(row=0,column=3,padx=5)

# Label5
label5=Label(frame1to0,text="5",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5.grid(row=0,column=4,padx=5)

# Label6
label6=Label(frame1to0,text="6",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6.grid(row=0,column=5,padx=5)

# Label7
label7=Label(frame1to0,text="7",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7.grid(row=0,column=6,padx=5)

# Label8
label8=Label(frame1to0,text="8",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8.grid(row=0,column=7,padx=5)

# Label9
label9=Label(frame1to0,text="9",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9.grid(row=0,column=9,padx=5)

# Label0
label10=Label(frame1to0,text="0",bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label10.grid(row=0,column=10,padx=5)

# FrameQToP
frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1,column=0)

# Label-q
labelq=Label(frameqtop,text="Q",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelq.grid(row=0,column=0,padx=5,pady=5)

# Label-w
labelw=Label(frameqtop,text="W",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelw.grid(row=0,column=1,padx=5,pady=5)

# Label-e
labele=Label(frameqtop,text="E",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labele.grid(row=0,column=2,padx=5,pady=5)

# Label-r
labelr=Label(frameqtop,text="R",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelr.grid(row=0,column=3,padx=5,pady=5)

# Label-t
labelt=Label(frameqtop,text="T",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelt.grid(row=0,column=4,padx=5,pady=5)

# Label-y
labely=Label(frameqtop,text="Y",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labely.grid(row=0,column=5,padx=5,pady=5)

# Label-u
labelu=Label(frameqtop,text="U",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelu.grid(row=0,column=6,padx=5,pady=5)

# Label-i
labeli=Label(frameqtop,text="I",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeli.grid(row=0,column=7,padx=5,pady=5)

# Label-o
labelo=Label(frameqtop,text="O",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelo.grid(row=0,column=8,padx=5,pady=5)

# Label-p
labelp=Label(frameqtop,text="P",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelp.grid(row=0,column=9,padx=5,pady=5)

# FrameAToL
frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0)

# Label-a
labela=Label(frameatol,text="A",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labela.grid(row=0,column=0,padx=5,pady=5)

# Label-s
labels=Label(frameatol,text="S",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labels.grid(row=0,column=1,padx=5,pady=5)

# Label-d
labeld=Label(frameatol,text="D",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeld.grid(row=0,column=2,padx=5,pady=5)

# Label-f
labelf=Label(frameatol,text="F",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelf.grid(row=0,column=3,padx=5,pady=5)

# Label-g
labelg=Label(frameatol,text="G",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelg.grid(row=0,column=4,padx=5,pady=5)

# Label-h
labelh=Label(frameatol,text="H",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelh.grid(row=0,column=5,padx=5,pady=5)

# Label-j
labelj=Label(frameatol,text="J",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelj.grid(row=0,column=6,padx=5,pady=5)

# Label-k
labelk=Label(frameatol,text="K",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelk.grid(row=0,column=7,padx=5,pady=5)

# Label-l
labell=Label(frameatol,text="L",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labell.grid(row=0,column=8,padx=5,pady=5)

# FrameZToM
frameztom=Frame(keyboard_frame)
frameztom.grid(row=3,column=0) 

# Label-z
labelz=Label(frameztom,text="Z",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelz.grid(row=0,column=0,padx=5,pady=5)

# Label-x
labelx=Label(frameztom,text="X",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelx.grid(row=0,column=1,padx=5,pady=5)

# Label-c
labelc=Label(frameztom,text="C",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelc.grid(row=0,column=2,padx=5,pady=5)

# Label-v
labelv=Label(frameztom,text="V",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelv.grid(row=0,column=3,padx=5,pady=5)

# Label-b
labelb=Label(frameztom,text="B",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelb.grid(row=0,column=4,padx=5,pady=5)

# Label-n
labeln=Label(frameztom,text="N",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeln.grid(row=0,column=5,padx=5,pady=5)

# Label-m
labelm=Label(frameztom,text="M",bg="black",fg="white",font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelm.grid(row=0,column=6,padx=5,pady=5)

# SpaceFrame
space_frame=Frame(keyboard_frame)
space_frame.grid(row=4,column=0)

# SpaceLabel
space=Label(space_frame,bg="black",fg="white",font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
space.grid(row=0,column=0,padx=5,pady=5)

# Collecting Label_Numbers
label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label10]

# Collecting Alphabets
label_alphabets=[labela,labelb,labelc,labeld,labele,labelf,labelg,labelh,labeli,labelj,labelk,labell,labelm,labeln,labelo,labelp,labelq,labelr,labels,labelt,labelu,labelv,labelw,labelx,labely,labelz]

# Collecting Space
label_space=[space]

# Binding-Numbers
bind_numbers=['1','2','3','4','5','6','7','8','9','0']

# Binding-Captical Letters
binding_captical_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Binding-Small Letters
binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def changeBG(widget): 
    widget.config(bg='blue')
    widget.after(100,lambda:widget.config(bg='black'))


for numbers in range(len(bind_numbers)):
    root.bind(bind_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))

for alphabets in range(len(binding_captical_alphabets)):
    root.bind(binding_captical_alphabets[alphabets],lambda event,label=label_alphabets[alphabets]:changeBG(label))

for alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[alphabets],lambda event,label=label_alphabets[alphabets]:changeBG(label))

root.bind('<space>',lambda event:changeBG(label_space[0])) # Representing SpaceBar key as <space>


root.mainloop()