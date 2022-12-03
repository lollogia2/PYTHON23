from tkinter import messagebox


def error1():
    messagebox.showerror('ERRORE', 'Path non trovato! Prova a cambiare parole ...')


def fields_warning():
    messagebox.showwarning('Attenzione', 'Campi vuoti o caratteri errati!')
