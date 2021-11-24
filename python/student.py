import re

class Student:
    
    def __init__(self, name: str, email: str, _class: str, CGM: str, shift: str, status: str) -> None:
        self.__name = name
        self.__email = Student.validate_email(email)
        self.__class = _class
        self.__CGM = Student.validate_CGM(CGM)
        self.__shift = shift
        self.__status = Student.validate_status(status)
        
    @staticmethod
    def validate_email(email: str) -> str:
        
        pattern = re.compile('[a-z]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        email = input('Por favor, insira um e-mail válido! ')
        return Student.validate_email(email)
    
    @staticmethod
    def validate_CGM(CGM: str) -> str:
        
        pattern = re.compile('[0-9]{8,}')
        
        if pattern.match(CGM):
            return pattern
        
        CGM = input('Por favor, insira um CGM válido! ')
        return Student.validate_CGM(CGM)
    
    @staticmethod
    def validate_status(status: str) -> bool:
        
        options = ['ATIVO', 'INATIVO']
        
        if status.upper() in options:
            return status
        
        status = input('Por favor, insira um status válido! ').upper()
        return Student.validate_status(status)
        