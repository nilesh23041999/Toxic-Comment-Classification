#!/usr/bin/python3
from airflow.api.client.local_client import Client
from tkinter import *
from PIL import ImageTk, Image
from youtube import main_yt

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)    
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0')




############ third page function #####################

def page_three_submit():
    inputValue=text_3.get("1.0",END)
    print(f'TestBox data::\n {inputValue}')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)    
    text_3.delete('1.0', END)

    
def page_three_back():
    root3.destroy()
    main_page()

def page_three():
    try:
        root.destroy()
    except:
        pass
    global root3,text_3
    root3 = Tk()
    root3.geometry("1366x768")
    root3.title("TOXIC COMMENT CLASSIFICATION GUI")
    
    root3.configure(bg='#F3F3F3')

    #BACK GROUND IMAGE
    load = Image.open('images/4.png')
    render = ImageTk.PhotoImage(load)
    main_image = Label(root3,image = render)
    main_image.place(x = -40, y = 0)


    #HEADING
    h1_img = PhotoImage(file = 'images/4_title.png')
    h1 = Button(root3,image = h1_img,bd = 0,bg='#F3F3F3')
    h1.place(x = 150,y = 30)

    #FRAME
    f2 = Frame(root3,width = 650,height = 350,bd = 0)
    f2.place(x = 380,y=180,width = 650,height = 350)

    
    scroll = Scrollbar(f2)
    scroll.pack(side=RIGHT, fill=Y)

    # Text Widget
    text_3 = Text(f2,yscrollcommand=scroll.set)
    text_3.pack(side=LEFT)

    # Configure the scrollbars
    scroll.config(command=text_3.yview)


    #BUTTONS
    b1_img = PhotoImage(file = 'images/back.png')
   #b1 = Button(root3,image = b1_img,bd = 0,bg = "#F3F3F3",command = page_three_back)
   # b1.place(x = 480,y = 550)


    b2_img = PhotoImage(file = 'images/submit.png')
    b2 = Button(root3,image = b2_img,bd = 0,bg = "#F3F3F3",command = page_three_submit)
    b2.place(x = 780,y = 550)

    
    root3.mainloop()



############ second page functions ###################
def page_two_submit():
    inputValue=text_2.get("1.0",END)
    #print(f'TestBox data::\n {inputValue}')
    main_yt(inputValue.strip())
    text_2.delete('1.0', END)
    
def page_two_back():
    root2.destroy()
    main_page()
    

def page_two():
    try:
        root.destroy()
    except:
        pass
    global root2,text_2
    root2 = Tk()
    root2.geometry("1366x768")
    root2.title("TOXIC COMMENT CLASSIFICATION GUI")
    
    root2.configure(bg='#DEDEDE')

    #BACK GROUND IMAGE
    load = Image.open('images/3r.png')
    render = ImageTk.PhotoImage(load)
    main_image = Label(root2,image = render)
    main_image.place(x = -40, y = 0)


    #HEADING
    h1_img = PhotoImage(file = 'images/3_title.png')
    h1 = Button(root2,image = h1_img,bd = 0,bg='#DEDEDE')
    h1.place(x = 250,y = 30)

    #FRAME
    f2 = Frame(root2,width = 650,height = 350,bd = 0)
    f2.place(x = 330,y=130,width = 650,height = 350)

    
    scroll = Scrollbar(f2)
    scroll.pack(side=RIGHT, fill=Y)

    # Text Widget
    text_2 = Text(f2,yscrollcommand=scroll.set)
    text_2.pack(side=LEFT)

    # Configure the scrollbars
    scroll.config(command=text_2.yview)


    #BUTTONS
    b1_img = PhotoImage(file = 'images/back.png')
    b1 = Button(root2,image = b1_img,bd = 0,bg = "#CBCBCB",activebackground='#CBCBCB',command = page_two_back)
    b1.place(x = 430,y = 500)


    b2_img = PhotoImage(file = 'images/submit.png')
    b2 = Button(root2,image = b2_img,bd = 0,bg = "#CBCBCB",activebackground='#CBCBCB',command = page_two_submit)
    b2.place(x = 730,y = 500)

    
    root2.mainloop()


############ first page functions ####################
def page_one_submit():
    inputValue=text_1.get("1.0",END)
    #print(f'twitter::\n {inputValue}')
    c = Client(None, None)
    c.trigger_dag(dag_id='Project', conf={"Keyword":inputValue.strip(),"time":5})
    text_1.delete('1.0', END)
    
def page_one_back():
    root1.destroy()
    main_page()


def page_one():
    try:
        root.destroy()
    except:
        pass
    global root1,text_1
    root1 = Tk()
    root1.geometry("1366x768")
    root1.title("TOXIC COMMENT CLASSIFICATION GUI")
    root1.configure(bg='#EEEAE7')



    #BACK GROUND IMAGE
    load = Image.open('images/2.png')
    render = ImageTk.PhotoImage(load)
    main_image = Label(root1,image = render)
    main_image.place(x = 0, y = 0)


    #HEADING
    h1_img = PhotoImage(file = 'images/2_title.png')
    h1 = Button(root1,image = h1_img,bd = 0)
    h1.place(x = 50,y = 100)



    #FRAME
    f1 = Frame(root1,width = 650,height = 350,bd = 0)
    f1.place(x = 450,y=250,width = 650,height = 350)

    
    scroll = Scrollbar(f1)
    scroll.pack(side=RIGHT, fill=Y)

    # Text Widget
    text_1 = Text(f1,yscrollcommand=scroll.set)
    text_1.pack(side=LEFT)

    # Configure the scrollbars
    scroll.config(command=text_1.yview)


    #BUTTONS
    b1_img = PhotoImage(file = 'images/back.png')
    b1 = Button(root1,image = b1_img,bd = 0,bg = "#ECE8E5",activebackground='#ECE8E5',command = page_one_back)
    b1.place(x = 550,y = 630)


    b2_img = PhotoImage(file = 'images/submit.png')
    b2 = Button(root1,image = b2_img,bd = 0,bg = "#ECE8E5",activebackground='#ECE8E5',command = page_one_submit)
    b2.place(x = 850,y = 630)
    
    root1.mainloop()




################### main page ######################
    
def main_page():
    global root
    root = Tk()
    root.geometry("1366x768")
    root.title("TOXIC COMMENT CLASSIFICATION GUI")
    root.configure(bg='#EEEAE7')


    #BACK GROUND IMAGE
    load = Image.open('images/1.png')
    render = ImageTk.PhotoImage(load)
    main_image = Label(root,image = render)
    main_image.place(x = 0, y = 0)

    #HEADING
    h1_img = PhotoImage(file = 'images/TOXIC.png')
    h1 = Button(root,image = h1_img,bd = 0)
    h1.place(x = 100,y = 100)

    h2_img = PhotoImage(file = 'images/COMMENTS.png')
    h2 = Button(root,image = h2_img,bd = 0,bg = "#E5E1DC")
    h2.place(x = 300,y = 100)

    h3_img = PhotoImage(file = 'images/DETECTION.png')
    h3 = Button(root,image = h3_img,bd = 0,bg = "#D8D0CC")
    h3.place(x = 660,y = 100)

    #BUTTONS
    b1_img = PhotoImage(file = 'images/b1.png')
    b1 = Button(root,image = b1_img,bd = 0,bg = "#EDE9E6",activebackground = "#EDE9E6",command = page_one)
    b1.place(x = 300,y = 300)



    b2_img = PhotoImage(file = 'images/b2.png')
    b2 = Button(root,image = b2_img,bd = 0,bg = "#EDE9E6",activebackground = "#EDE9E6",command = page_two)
    #b2.place(x = 300,y = 400)

    b3_img = PhotoImage(file = 'images/b3.png')
    b3 = Button(root,image = b3_img,bd = 0,bg = "#EDE9E6",activebackground = "#EDE9E6",command = page_three)
   # b3.place(x = 300,y = 500)
    
    root.mainloop()




if __name__ == '__main__':
    main_page()

