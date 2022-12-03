from tkinter import messagebox


def fields():
    messagebox.showerror('ERRORE', 'Campi vuoti o caratteri errati!')


def general_warning():
    messagebox.showwarning('Attenzione', 'Conessione non trovata! Prova a cambiare parole ...')
