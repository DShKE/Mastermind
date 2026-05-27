import tkinter as tk
import random

def raisee(x):
    for i in root.winfo_children():
        if i != x:
            i.pack_forget()
    x.pack(fill="both", expand=True)

def initgame():
    global numrange, pegamt, numrangeslider, pegamtslider, frame2, frame3,inpfields, secretlist, correctlabel, totalcorrectlabel, trieslabel
    root.minsize(1,1)
    numrange=numrangeslider.get()
    pegamt=pegamtslider.get()
    frame2 = tk.Frame(root)
    frame2.pack(fill="both", expand=True)
    submitbutton=tk.Button(frame2, text="Submit", command=checkk)
    submitbutton.grid(row=0, column=0)
    correctlabel = tk.Label(frame2, text="correct: 0")
    correctlabel.grid(row=1, column=0)
    totalcorrectlabel = tk.Label(frame2, text="total correct: 0")
    trieslabel = tk.Label(frame2, text="tries: 0")
    if pegamt > 2:
        totalcorrectlabel.grid(row=1, column=pegamt-1)
        trieslabel.grid(row=1, column=int(pegamt/2))
    else:
        totalcorrectlabel.grid(row=1, column=2)
        trieslabel.grid(row=1, column=1)

    inpfields = [None] * pegamt
    for i in range(pegamt):
        inpfields[i]=tk.Entry(frame2, width=2, justify='center')
        inpfields[i].grid(row=2, column=i)
    raisee(frame2)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    secretlist = [str(random.randint(1, numrange)) for i in range(pegamt)]
    secretlistlabel = tk.Label(frame3, text=f"answer: {",".join(secretlist)}")
    secretlistlabel.pack()


def checkk():
    global correctlabel, totalcorrectlabel, inpfields, secretlist, inpp, frame3, endlabel, totalcorrect, correct, tries
    tries+=1
    trieslabel.config(text=f"tries: {tries}")
    totalcorrect, correct = 0, 0
    inpp = [None] * len(inpfields)
    for i in range(len(inpfields)):
        inpp[i] = inpfields[i].get().strip()
        if(inpp[i] == secretlist[i]):
            correct += 1
            correctlabel.config(text=f"correct: {correct}")
        if(inpp[i] in secretlist):
            if inpp.count(inpp[i]) <= secretlist.count(str(inpp[i])):
                totalcorrect+=1
            correctlabel.config(text=f"correct: {correct}")
        totalcorrectlabel.config(text=f"total correct: {totalcorrect}")
    if correct == len(secretlist):
        root.minsize(1,1)
        raisee(frame3)
        endlabel.config(text="u ar winr")
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
    if tries >= 10:
        root.minsize(1,1)
        raisee(frame3)
        endlabel.config(text="u ar loser")
        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
def initmygui():
    global frame1, frame2, numrangeslider, pegamtslider, dialog, inp, endlabel, frame3, root, tries
    try:
        root.destroy()
    except:
        pass
    root = tk.Tk()
    root.title("Mast3r M1nd")
    tries = 0
    frame1=tk.Frame(root)
    frame1.pack(fill="both", expand=True)
    pegamtslider = tk.Scale(frame1, from_=1, to=5, orient='horizontal', length=200)
    pegamtslider.grid(row=0, column=3)
    numrangeslider = tk.Scale(frame1, from_=1, to=5, orient='horizontal', length=200)
    numrangeslider.grid(row=1, column=3)
    pegnumtitle = tk.Label(frame1, text="number of PEGS")
    pegnumtitle.grid(row=0, column=0)
    numamtitle = tk.Label(frame1, text="range of numbers")
    numamtitle.grid(row=1, column=0)
    contbutton=tk.Button(frame1, text="Continue", command=initgame)
    contbutton.grid(row=2, column=3)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    frame3 = tk.Frame(root)
    endlabel = tk.Label(frame3)
    endlabel.pack()
    againbutton = tk.Button(frame3, text="Again", command=initmygui)
    againbutton.pack()

initmygui()

root.mainloop()