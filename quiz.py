from tkinter import *
from words import list
import time
import random
from tkinter import messagebox
def main():
    def reset():
        window.destroy()
        main()
    def hint():
        label5  = Label(window,font=("Arial",20),text=word[:-1]+' _')
        label5.pack()
    def new_label():
        label  = Label(window,font=("Arial",20),text='_ '+word[1:-1]+' _')
        label.pack()
    def check():
         if entry.get().lower()==word:
             label  = Label(window ,bg='#F5D624',font=("Arial",20),text='Correct!')
             label.pack()
         else:
             label2  = Label(window,bg='#E62F28',font=("Arial",20),text="Incorrect!")
             label2.pack()
        
    def  new_window():
         answer=(messagebox.askokcancel(title='this is quizy bezy',message="this is quiz game made my JIGATA "+'\n' 'the point is to guess the word without knowing the first and the last letter',icon='info'))
    window = Tk()
    
    WIDTH=500
    HEIGHT =500
    window.geometry("420x420")
    window.title("quizy bezy")
    #icon = PhotoImage(file='C:\\Users\\DELL\\Desktop\\photo\\illustration-de-la-conception-3d-jeu-questionnaire-sur-l-icone-orange-epyf62.png')
    #bg= PhotoImage(file='C:\\Users\\DELL\\Desktop\\photo\\My project-1.png')
    #window.iconphoto(True,icon)
    window_width = WIDTH
    window_height = HEIGHT
    my_label = Label(window,)#image=bg
    my_label.place(x=0,y=0,relwidth=1,relheight=1)
    label0  = Label(window,bg = '#2788CC',font=("Cambria",20),text="WELCOME")
    label0.pack()
    
    About_button =Button(window,text='About',command=new_window,font=("Cambria",20)).place(x=5,y=5,)
    hint_button =Button(window,text='HINT',command=hint,font=("Cambria",20)).place(x=410,y=5,)
    button1 =Button(window,text='GET A WORD',command=new_label,font=("Cambria",20)).pack()
    entry = Entry(window,text='answer',font=("Cambria",20),relief=RAISED) 
    entry.pack()
    submit_button =Button(window,text='submit',command=check,font=("Cambria",20),state=ACTIVE).pack()
    reset_button =Button(window,text='reset',command=reset,font=("Cambria",20),state=ACTIVE).pack()
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    word = random.choice(list)
    
    '''
    xVelocity = 3.5
    yVelocity = 3.5
    canvas = Canvas(window, height=50,width=50)
    canvas.pack()
    photoimage = PhotoImage(file='C:\\Users\\DELL\\Desktop\\photo\\quiz.png')
    myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)
    while True:
     coordinates = canvas.coords(myimage)
     print (coordinates)
     
     if (coordinates[0]>=305 or coordinates[0]<0):
        xVelocity= -xVelocity    
     if (coordinates[1]>=305 or coordinates[1]<0):
          yVelocity= -yVelocity
     canvas.move(myimage,xVelocity,yVelocity)
     window.update()#very imp
     time.sleep(0.01)
     '''
    window.mainloop()
    
main()

    




















