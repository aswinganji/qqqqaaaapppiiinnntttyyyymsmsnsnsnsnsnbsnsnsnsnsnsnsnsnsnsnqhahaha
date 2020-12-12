from tkinter import*
import random
root = Tk()
root.title("Geome")
root.geometry("400x400")

randompoll = Label(root)
sorli = Label(root)

def ran():
    random_in=random.sample(range(2788,29100),5)
    randompoll["text"]="qwerty list" + str(random_in)
    random_in.sort()
    
    sorli["text"]="Monster List " + str(random_in)
    
btn = Button(root,text = "GenerateUnrando" ,command = ran)
btn.place(relx = 0.5,rely = 0.5, anchor = CENTER)
randompoll.place(relx = 0.5,rely = 0.7, anchor = CENTER)
sorli.place(relx = 0.5,rely = 0.9, anchor = CENTER)

btn.pack()
randompoll.pack()
sorli.pack()

root.mainloop()