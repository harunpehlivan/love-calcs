from tkinter import *
from random import randint

#Please don't change the CODE!

#window
prozor = Tk()
prozor.title('love calc')
prozor.config(width=700, height=500)
prozor.config(background='#f9e0ef')
prozor.config(cursor='spider')

#title
naslov = Label(prozor,
               text='LOVE CALCULATOR',
               background='#f9e0ef',
               fg='#fc79c5',
               font=('Chilanka', 26))
naslov.place(x=190, y=20)

#female name
z = Label(prozor,
          text='Female:',
          background='#f99dd3',
          fg='BLACK',
          font=('Arial', 16))
z.place(x=100, y=90)

#male name
m = Label(prozor,
          text='Male:',
          background='#f99dd3',
          fg='BLACK',
          font=('Arial', 16))
m.place(x=450, y=90)

#textbox
z_unos = Entry(prozor, width=20)
z_unos.place(x=100, y=120)

m_unos = Entry(prozor, width=20)
m_unos.place(x=450, y=120)


#random number generator
def izracunaj():
    n = randint(1, 100)
    return n


#main function
def provjeri_prikazi():
    if len(z_unos.get()) == 0 or len(m_unos.get()) == 0:
        rez = Label(prozor,
                    text='Enter name!',
                    background='#fc79c5',
                    fg='white',
                    font=('Chilanka', 26))
        rez.place(x=290, y=260)

    else:

        rez = Label(prozor,
                    text='        ' + str(izracunaj()) + '%      ',
                    font=('Chilanka', 26),
                    background='#fc79c5',
                    fg='white')
        rez.place(x=290, y=260)



#button
gumb = Button(
    prozor,
    text='Calculate!',
    font=('Arial', 20),
    background='black',
    fg='white',
    command=lambda: [provjeri_prikazi(), izracunaj()])
gumb.place(x=290, y=180)

#image
logo = PhotoImage(file='heart.gif')
okvir = Label(prozor, image=logo, borderwidth=0)
okvir.place(x=640, y=300)

prozor.mainloop()
