from tkinter import Tk, ttk
from tkinter import *

'''window = Tk()
window.title('Edutech Manager')

mainframe = ttk.Frame(window, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

ttk.Button(mainframe, text='Inserir Professor').grid(column=2, row=1, sticky=(W,E))
ttk.Button(mainframe, text='Inserir Aluno').grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text='Visualizar Professores').grid(column=2, row=3, sticky=(W,E))
ttk.Button(mainframe, text='Visualizar Alunos').grid(column=2, row=4, sticky=(W,E))
ttk.Label(mainframe).grid(column=2, row=5, sticky=(W,E))
ttk.Button(mainframe, text='Sair', command=exit).grid(column=2, row=6, sticky=(W,E))

for child in mainframe.winfo_children():
    pass
    child.grid_configure(padx=10, pady=2.5)

window.mainloop()
'''
class UserInterface:
    
    def __init__(self) -> None:
        self.__root = Tk()
        self.__mainframe = ttk.Frame(self.__root, padding='3 3 12 12')
        self.__configure_main_window()
        self.__set_all_buttons()
        
        self.__root.mainloop()
        
    def __configure_main_window(self) -> None:
        self.__mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        
    def __set_all_buttons(self) -> None:
        ttk.Button(self.__mainframe, text='Inserir Professor', command=self.__set_insert_teacher_screen).grid(column=2, row=1, sticky=(W,E))
        ttk.Button(self.__mainframe, text='Inserir Aluno', command=self.__set_insert_students_screen).grid(column=2, row=2, sticky=(W,E))
        ttk.Button(self.__mainframe, text='Visualizar Professores').grid(column=2, row=3, sticky=(W,E))
        ttk.Button(self.__mainframe, text='Visualizar Alunos').grid(column=2, row=4, sticky=(W,E))
        ttk.Label(self.__mainframe).grid(column=2, row=5, sticky=(W,E))
        ttk.Button(self.__mainframe, text='Sair', command=exit).grid(column=2, row=6, sticky=(W,E))

        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=10, pady=2.5)
    
    def __set_insert_teacher_screen(self) -> None:
        window = Toplevel(self.__root)
            
    def __set_insert_students_screen(self) -> None:
        window = Toplevel(self.__root)
        
        
UserInterface()