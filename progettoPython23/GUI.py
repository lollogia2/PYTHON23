from tkinter import *
import errors
import find_word as fw
import inspect


# --------------------------------parte grafica--------------------------------


def setup():
    gui = Tk()
    gui.title('FindPath')
    gui.geometry('400x300')
    gui.configure(bg='dark grey')
    gui.resizable(0, 0)
    title = Label(gui,
                  text="BIG DICTIONARY",
                  fg="MediumOrchid4",
                  background='dark grey',
                  font=('Ariel', 18, 'bold italic'))
    title.grid(row=0)
    L1 = Label(gui,
               text='Parola di partenza: ',
               fg='red', background='dark grey',
               font=('Ariel', 11, 'bold italic'))
    L1.grid(row=1, column=0)
    E1 = Entry(gui, bd=5)
    E1.grid(row=1, column=1)
    L2 = Label(gui,
               text='Parola di arrivo: ',
               fg='red',
               background='dark grey',
               font=('Ariel', 11, 'bold italic'))
    L2.grid(row=2, column=0)
    E2 = Entry(gui, bd=5)
    E2.grid(row=2, column=1)
    btn = Button(gui,
                 text='Calcola il percorso !',
                 bd='5',
                 font=('Ariel', 9, 'bold'))
    btn.grid(row=3)
    result = Label(text='',
                   fg='MediumOrchid4',
                   background='dark grey',
                   font=('Ariel', 11, 'bold'))
    result.grid(row=4)

    def run1(e1, e2):
        if e1 != '' and e2 != '' and e1.isalpha() and e2.isalpha():
            fw.reset_counter()
            dictionary = fw.get_dictionary_word_list()  # list of words
            graph = fw.make_graph(dictionary)
            try:
                a = " -> ".join(fw.walk_graph(graph, dictionary, e1.lower(), e2.lower()))
                result.config(text=a)
            except TypeError:
                errors.error1()
        else:
            errors.fields_warning()

    btn.config(command=lambda: run1(E1.get(), E2.get()))
    gui.mainloop()
