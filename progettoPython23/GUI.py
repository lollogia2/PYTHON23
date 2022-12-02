from tkinter import *
import errors
import find_word as fw


# --------------------------------parte grafica--------------------------------


def setup():
    gui = Tk(className='FindPath')
    gui.geometry('400x300')
    gui.configure(background='dark grey')
    label = Label(gui, text="BIG DICTIONARY", fg="MediumOrchid4", background='dark grey',
                  font=('Ariel', 18, 'bold italic'))
    label.grid(row=0)
    L1 = Label(gui, text='Parola di partenza: ', fg='red', background='dark grey', font=('Ariel', 11, 'bold italic'))
    L1.grid(row=1, column=0)
    E1 = Entry(gui, bd=5)
    E1.grid(row=1, column=1)
    L2 = Label(gui, text='Parola di arrivo: ', fg='red', background='dark grey', font=('Ariel', 11, 'bold italic'))
    L2.grid(row=2, column=0)
    E2 = Entry(gui, bd=5)
    E2.grid(row=2, column=1)
    btn = Button(gui, text='Calcola il percorso !', bd='5', font=('Ariel', 9, 'bold'))
    btn.grid(row=3)

    def run1(E1, E2):
        if E1 != '' and E2 != '' and E1.isalpha() and E2.isalpha():
            dictionary = fw.get_dictionary_word_list()  # list of words
            graph = fw.make_graph(dictionary)
            try:
                a = " -> ".join(fw.walk_graph(graph, dictionary, E1, E2))
                result = Label(text=a, fg='MediumOrchid4', background='dark grey', font=('Ariel', 11, 'bold'))
                result.grid(row=4)
            except:
                errors.fields2()  # gestione eccezione nel caso vengano
                # inserite parole assurde (es. 'aaaaaaa')
        else:
            errors.fields()

    btn.config(command=lambda: run1(E1.get(), E2.get()))
    gui.mainloop()
