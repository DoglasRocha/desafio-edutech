from tkinter import *
from tkinter import ttk

class InsertStudentScreen:
    
    def __init__(self, root) -> None:
        self.__window = Toplevel(root)
        self.__mainframe = ttk.Frame(self.__window, padding='5')
        self.__name = StringVar()
        self.__email = StringVar()
        self.__class = StringVar()
        self.__CGM = StringVar()
        self.__shift = StringVar()
        self.__status = StringVar()
        self.__teacher = StringVar()
        
        self.__set_buttons()
        self.__set_labels()
        self.__set_entries()
        self.__configure_screen()
        
    def __configure_screen(self) -> None:
        self.__window.title('Inserir Aluno')
        self.__mainframe.grid(column=0, row=0, sticky=(N,S,W,E))
        self.__window.columnconfigure(0, weight=1)
        self.__window.rowconfigure(0, weight=1)
        
        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=10, pady=2.5)
    
    def __set_buttons(self) -> None:
        ttk.Button(self.__mainframe, 
                   text='Cancelar', 
                   command=self.__window.destroy).grid(column=5, row=6,
                                                       sticky=(W,E))
        ttk.Button(self.__mainframe,
                   text='Criar Aluno',
                   command=self.__try_to_create_student).grid(column=6,
                                                              row=6,
                                                              sticky=(W,E))
                   
    def __set_labels(self) -> None:
        ttk.Label(self.__mainframe, text='Nome: ').grid(column=1, 
                                                        row=1)
        ttk.Label(self.__mainframe, text='E-mail: ').grid(column=3, 
                                                          row=1)
        ttk.Label(self.__mainframe, text='Turma: ').grid(column=5, 
                                                         row=1)
        
        ttk.Label(self.__mainframe, text='CGM: ').grid(column=1, 
                                                       row=2)
        ttk.Label(self.__mainframe, text='Turno: ').grid(column=3, 
                                                         row=2)
        
        ttk.Label(self.__mainframe, text='Professor: ').grid(column=1, 
                                                             row=3)
        ttk.Label(self.__mainframe, text='Status: ').grid(column=3, 
                                                          row=3)
            
    def __set_entries(self) -> None:
        ttk.Entry(self.__mainframe, textvariable=self.__name).grid(
            column=2, row=1)
        ttk.Entry(self.__mainframe, textvariable=self.__email).grid(
            column=4, row=1)
        ttk.Entry(self.__mainframe, textvariable=self.__class).grid(
            column=6, row=1)
        
        ttk.Entry(self.__mainframe, textvariable=self.__CGM).grid(
            column=2, row=2)
        ttk.Radiobutton(self.__mainframe, variable=self.__shift,
                  text='M', value='M').grid(column=4, row=2, 
                                            sticky=W)
        ttk.Radiobutton(self.__mainframe, variable=self.__shift,
                  text='T', value='T').grid(column=5, row=2, 
                                            sticky=W)
        
        ttk.Entry(self.__mainframe, textvariable=self.__teacher).grid(
            column=2, row=3)            
        ttk.Radiobutton(self.__mainframe, variable=self.__status,
                        text='ATIVO', value='ATIVO').grid(
            column=4, row=3, sticky=W)
        ttk.Radiobutton(self.__mainframe, variable=self.__status,
                        text='INATIVO', value='INATIVO').grid(
            column=5, row=3, sticky=W)      
            
    def __try_to_create_student(self) -> None:
        print(self.__name.get())
    
