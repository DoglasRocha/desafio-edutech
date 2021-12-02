import pyodbc

def connect_to_database() -> pyodbc.Cursor:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;UID=SA;PWD=****')
    cnxn.autocommit = True
    cursor = cnxn.cursor()
    
    try:
        cursor.execute('USE EdutechDB;')
        
    except pyodbc.OperationalError:
        cursor.execute('CREATE DATABASE EdutechDB;')
        cursor.execute('''
                       CREATE TABLE Professores (
                            Nome VARCHAR(100) NOT NULL PRIMARY KEY,
                            Email VARCHAR(100) NOT NULL,
                            Turmas VARCHAR(500) NOT NULL,
                            Turno CHAR NOT NULL
                       );
                       ''')
        
        cursor.execute('''
                       CREATE TABLE Alunos (
                            Nome VARCHAR(100) NOT NULL,
                            Email VARCHAR(100) NOT NULL,
                            Turma VARCHAR(50) NOT NULL,
                            CGM INT NOT NULL,
                            Turno CHAR NOT NULL,
                            Status_ VARCHAR(10) NOT NULL,
                            Professor VARCHAR(100) NOT NULL FOREIGN KEY REFERENCES Professores(Nome)
                       );
                       ''')
        
    return cnxn