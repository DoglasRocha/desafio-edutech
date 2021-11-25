import re
from cursor import connect_to_database

class Student:
    
    def __init__(self, name: str, email: str, _class: str, CGM: str, shift: str, status: str, teacher: str) -> None:
        self.__name = name
        self.__email = Student.validate_email(email)
        self.__class = _class
        self.__CGM = Student.validate_CGM(CGM)
        self.__shift = Student.validate_shift(shift)
        self.__status = Student.validate_status(status)
        self.__teacher = teacher
        
        self.send_data_to_database()
        
    def send_data_to_database(self) -> None:
        cursor = connect_to_database()
        
        cursor.execute(f'''INSERT Alunos 
                           VALUES (
                                '{self.__name}', '{self.__email}', '{self.__class}',
                                {self.__CGM}, '{self.__shift}', '{self.__status}',
                                '{self.__teacher}'
                           )''')
        
        cursor.close()
    
    @staticmethod
    def validate_email(email: str) -> str:
        
        pattern = re.compile('[a-z.]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        email = input('Por favor, insira um e-mail válido! ')
        return Student.validate_email(email)
    
    @staticmethod
    def validate_CGM(CGM: str) -> str:
        
        pattern = re.compile('[0-9]{8,}')
        
        if pattern.match(CGM):
            return CGM
        
        CGM = input('Por favor, insira um CGM válido! ')
        return Student.validate_CGM(CGM)
    
    @staticmethod
    def validate_status(status: str) -> bool:
        
        options = ['ATIVO', 'INATIVO']
        
        if status.upper() in options:
            return status
        
        status = input('Por favor, insira um status válido! ').upper()
        return Student.validate_status(status)
    
    @staticmethod
    def validate_shift(shift: str) -> str:
        
        options = ['M', 'T']
        
        if shift.upper() in options:
            return shift
        
        shift = input('Por favor, insira um turno válido! ').upper()
        return Student.validate_shift(shift)
    