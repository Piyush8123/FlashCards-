from tkinter import *
import random

root = Tk()
root.title("FlashCards App")
root.geometry("700x500")
root.config(background = '#358597')

# Create submit function of add
def su():
        global a,b,c,d,ans
        ans.grid_forget()
        c = StringVar
        c = str(a+b)
        if i.get() == c:
            ans = Label(new, text="Yes!! Your answer is correct." +" "+str(a) + "+" + str(b) + "=" +"  "+ i.get(),font = ("Helvetica",20),bg = 'light green')
            ans.grid(row=3, column=0,pady = 15)
        else:
            ans = Label(new, text="Oops!! Your answer is incorrect." +"  "+str(a) + "+" + str(b) + "=" +"  "+ c,font = ("Helvetica",20),bg = 'light green')
            ans.grid(row=3, column=0,pady = 15)

        i.delete(0, 'end')
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        d = Label(new,text=(a, "+", b), width=20, font=("Helvetica", 28), bg='#3D8C95')
        d.grid(row=0, column=0, padx=100, pady=50)

# Create addition function
def add():
    global i,new,ans,d,a,b

    new = Tk()
    new.title("Addition Card")
    new.geometry("700x500")
    new.config(background = '#F4B41A')
    # Create Menu for add
    add_menu = Menu(new)
    new.config(menu=add_menu)

    # Define Menu Items
    file = Menu(add_menu)
    add_menu.add_cascade(label="File", menu=file)
    file.add_command(label="Home", command = lambda : new.destroy())

    ans = Label(new)
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = StringVar
    c = str(a+b)

    d = Label(new, text = (a,"+",b) , width=20, font=("Helvetica", 28),bg='#3D8C95')
    d.grid(row=0, column=0, padx=100, pady=50)

    i = Entry(new,font = ("Helvetica",20))
    i.grid(row = 1,column = 0)

    btn = Button(new,text = "Submit My Answer",command = su)
    btn.grid(row = 2,column = 0,pady = 20)


    new.mainloop()
# Create submit function of subtraction
def cl():
    global a, b, c, d, ans
    ans.grid_forget()
    c = StringVar
    c = str(a - b)
    if i.get() == c:
        ans = Label(child, text="Yes!! Your answer is correct." + " " + str(a) + "-" + str(b) + "=" + "  " + i.get(),font=("Helvetica", 20),bg = "light green")
        ans.grid(row=3, column=0, pady=15)
    else:
        ans = Label(child, text="Oops!! Your answer is incorrect." + "  " + str(a) + "-" + str(b) + "=" + "  " + c,font=("Helvetica", 20),bg = "light green")
        ans.grid(row=3, column=0, pady=15)

    i.delete(0, 'end')
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    d = Label(child, text=(a, "-", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)

# Create subtraction function
def sub():

    global i,child,ans,d,a,b,c
    child = Tk()
    child.title("Subtraction Card")
    child.geometry("700x500")
    child.config(background="#F4B41A")

    # Create Menu for subtrat
    add_menu = Menu(child)
    child.config(menu=add_menu)

    # Define Menu Items
    file = Menu(add_menu)
    add_menu.add_cascade(label="File", menu=file)
    file.add_command(label="Home", command = lambda : child.destroy())

    ans = Label(child)
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = StringVar
    c = str(a-b)

    d = Label(child, text=(a, "-", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)

    i = Entry(child, font=("Helvetica", 20))
    i.grid(row=1, column=0)

    btn = Button(child, text="Submit My Answer", command=cl)
    btn.grid(row=2, column=0, pady=20)

    child.mainloop()

# Create submit function of multiplication
def ck():
    global a, b, c, d, ans
    ans.grid_forget()
    c = StringVar
    c = str(a * b)
    if i.get() == c:
        ans = Label(c1, text="Yes!! Your answer is correct." + " " + str(a) + "*" + str(b) + "=" + "  " + i.get(),font=("Helvetica", 20),bg = "light green")
        ans.grid(row=3, column=0, pady=15)
    else:
        ans = Label(c1, text="Oops!! Your answer is incorrect." + "  " + str(a) + "*" + str(b) + "=" + "  " + c,font=("Helvetica", 20),bg = "light green")
        ans.grid(row=3, column=0, pady=15)

    i.delete(0, 'end')
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    d = Label(c1, text=(a, "*", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)

# Create multiplication function
def mul():
    global i,c1,ans,d,a,b,c
    c1 = Tk()
    c1.title("Multiplication Card")
    c1.geometry("700x500")
    c1.config(background="#F4B41A")

    # Create Menu for multiply
    add_menu = Menu(c1)
    c1.config(menu=add_menu)

    # Define Menu Items
    file = Menu(add_menu)
    add_menu.add_cascade(label="File", menu=file)
    file.add_command(label="Home", command=lambda : c1.destroy())

    ans = Label(c1)
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = StringVar()
    c = str(a*b)

    d = Label(c1, text=(a, "*", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)

    i = Entry(c1, font=("Helvetica", 20))
    i.grid(row=1, column=0)

    btn = Button(c1, text="Submit My Answer", command=ck)
    btn.grid(row=2, column=0, pady=20)

    c1.mainloop()

# Create submit function of division
def cs():
    global a, b, c, d, ans
    ans.grid_forget()
    try:
        c = StringVar
        c = str(a // b)
        if i.get() == c:
            ans = Label(cd, text="Yes!! Your answer is correct." + " " + str(a) + "/" + str(b) + "=" + "  " + i.get(),
                        font=("Helvetica", 20),bg = "light green")
            ans.grid(row=3, column=0, pady=15)
        else:
            ans = Label(cd, text="Oops!! Your answer is incorrect." + "  " + str(a) + "/" + str(b) + "=" + "  " + c,
                        font=("Helvetica", 20),bg = "light green")
            ans.grid(row=3, column=0, pady=15)

    except:
        ans = Label(cd, text="Zero Division Error",font=("Helvetica", 20),bg = "light green")
        ans.grid(row=3, column=0)

    i.delete(0, 'end')
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    d = Label(cd, text=(a, "/", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)



# Create division function
def div():
    global i, cd, ans, d, a, b,c
    cd = Tk()
    cd.title("Division Card")
    cd.geometry("700x500")
    cd.config(background="#F4B41A")
    ans = Label(cd)

    # Create Menu for div
    add_menu = Menu(cd)
    cd.config(menu=add_menu)

    # Define Menu Items
    file = Menu(add_menu)
    add_menu.add_cascade(label="File", menu=file)
    file.add_command(label="Home", command=lambda: cd.destroy())

    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = StringVar()
    c = str(a//b)

    d = Label(cd, text=(a, "/", b), width=20, font=("Helvetica", 28), bg="#3D8C95")
    d.grid(row=0, column=0, padx=100, pady=50)

    i = Entry(cd, font=("Helvetica", 20))
    i.grid(row=1, column=0)

    btn = Button(cd, text="Submit My Answer", command=cs)
    btn.grid(row=2, column=0, pady=20)

    cd.mainloop()

# Create home function
def home():

    head = Label(root, text="Welcome to FlashCards Game!!", width="30", font=("Helvetica", 20))
    head.grid(row=1, column=1, padx=110, pady=10)

    card = Button(root, text="Addition Card", width="20", font=("Helvetica", 15), bg="#F4A897", command=add)
    card.grid(row=2, column=1, padx=110, pady=25)

    card = Button(root, text="Subtraction Card", width="20", font=("Helvetica", 15), bg="#F4A897", command=sub)
    card.grid(row=3, column=1, padx=110, pady=25)

    card = Button(root, text="Multiplication Card", width="20", font=("Helvetica", 15), bg="#F4A897", command=mul)
    card.grid(row=4, column=1, padx=110, pady=25)

    card = Button(root, text="Division Card", width="20", font=("Helvetica", 15), bg="#F4A897", command=div)
    card.grid(row=5, column=1, padx=110, pady=25)


# Create exit function
def ex():
    root.quit()

# Create Menu
main_menu = Menu(root)
root.config(menu = main_menu)

# Define Menu Items
var = Menu(main_menu)
main_menu.add_cascade(label = "MathCards",menu = var)
var.add_command(label = "Add",command = add)
var.add_command(label = "Subtract",command = sub)
var.add_command(label = "Multiply",command = mul)
var.add_command(label = "Divide",command = div)
var.add_separator()
var.add_command(label = "Home",command = home)
var.add_command(label = "Exit",command = ex)

head = Label(root,text = "Welcome to FlashCards Game!!",width = "30",font = ("Helvetica",20))
head.grid(row = 1,column = 1,padx = 110,pady = 10)

card = Button(root,text = "Addition Card",width = "20",font = ("Helvetica",15),bg = "#F4A897",command = add)
card.grid(row = 2,column = 1,padx = 110,pady = 25)

card = Button(root,text = "Subtraction Card",width = "20",font = ("Helvetica",15),bg = "#F4A897",command = sub)
card.grid(row = 3,column = 1,padx = 110,pady = 25)

card = Button(root,text = "Multiplication Card",width = "20",font = ("Helvetica",15),bg = "#F4A897",command = mul)
card.grid(row = 4,column = 1,padx = 110,pady = 25)

card = Button(root,text = "Division Card",width = "20",font = ("Helvetica",15),bg = "#F4A897",command = div)
card.grid(row = 5,column = 1,padx = 110,pady = 25)




root.mainloop()