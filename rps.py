from tkinter import *
import random


def clicked(event):
    global player_score
    global computer_score
    global compch
    randno = random.randint(1,3)
    if randno == 1:
        compch = "rock"
    elif randno == 2:
        compch = "paper"
    else:
        compch = "sisor"
    btext = event.widget.cget('text')
    lbx.insert(END,f"Your Entered Choice is: {btext}")
    lbx.insert(END, f"Computer Choice is: {compch}")
    lbx.insert(END, "***************")
    lbx2.delete(0,END)
    if btext == "rock":
        if compch == "rock":
            lbx.insert(END, "tie")
        elif compch =="paper":
            lbx.insert(END, "computers win")
           
            computer_score += 1
           
        elif compch =="sisor":
            lbx.insert(END, "You win")
            player_score += 1
           

    elif btext == "paper":
        if compch == "rock":
            lbx.insert(END, "You win")
            player_score += 1
            
        elif compch =="paper":
            lbx.insert(END, "tie")
            
        elif compch =="sisor":
            lbx.insert(END, "computers win")
            computer_score += 1
    else:  #btext= sisor
        if compch == "rock":
            lbx.insert(END, "computers win")
            computer_score += 1
           
        elif compch =="paper":
            lbx.insert(END, "You win")
            player_score += 1
           
        elif compch =="sisor":
            lbx.insert(END, "tie")
    lbx.delete(0,ACTIVE) 
    lbx2.insert(END,f'player score is: {player_score}')  
    lbx2.insert(END,f'computer score is: {computer_score}')
    
    
    
    
    




    
root = Tk()
root.geometry("1000x900")
root.title("Rock paper sisor")
player_score= 0
computer_score= 0
Label(root, text="Lets play!!!",font="comicsansms 25 bold", relief=SUNKEN).grid(row=0,column=3)
lbx=Listbox(root,bg="green",width=25,bd=4,font="comicsansms 19 bold",fg="yellow")
lbx.grid(row=1,column=2,sticky="nsew")
lbx.insert(END,"Enter your choice:")
lbx2 = Listbox(root,bg="yellow",width=20,bd=4,font="comicsansms 19 bold",fg="green")
lbx2.grid(row=1,column=4,sticky="nsew")
lbx2.insert(END, "SCORECARD")


b = Button(root, text="rock",bg="red",fg="white",activebackground="white",activeforeground="red",font="comicsansms 17 bold",bd=4)
b.grid(row=2, column=3,pady=3)
b.bind('<Button-1>' ,clicked)
b = Button(root, text="paper",bg="red",fg="white",activebackground="white",activeforeground="red",font="comicsansms 17 bold",bd=4)
b.grid(row=3, column=3,pady=3)
b.bind('<Button-1>' ,clicked)
b = Button(root, text="sisor",bg="red",fg="white",activebackground="white",activeforeground="red",font="comicsansms 17 bold",bd=4)
b.grid(row=4, column=3,pady=3)
b.bind('<Button-1>' ,clicked)

root.mainloop()
