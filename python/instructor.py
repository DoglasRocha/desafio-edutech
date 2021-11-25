import re

class Instructor:
    
    def __init__(self, name: str, email: str, classes: list, shift: str) -> None:
        self.__name = name
        self.__email = Instructor.validate_email(email)
        self.__classes = classes
        self.__shift = shift
        
    @staticmethod
    def validate_email(email: str) -> str:
        pattern = re.compile('[a-z.]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        email = input('Por favor, insira um e-mail válido! ')
        return Instructor.validate_email(email)