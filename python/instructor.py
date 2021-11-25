import re
from program_messenger import ProgramMessenger

class Instructor:
    
    def __init__(self, name: str, email: str, classes: list, 
                 shift: str) -> None:
        self.__name = name
        self.__email = Instructor.validate_email(email)
        self.__classes = classes
        self.__classes_str = self.convert_classes_list_to_string()
        self.__shift = Instructor.validate_shift(shift)
        
        self.send_to_database()
        
    def send_data_to_database(self) -> None:
        ProgramMessenger.insert_teacher_into_database(self.__name,
                                                      self.__email,
                                                      self.__classes_str,
                                                      self.__shift)
        
    @staticmethod
    def validate_email(email: str) -> str:
        pattern = re.compile('[a-z.]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        email = input('Por favor, insira um e-mail válido! ')
        return Instructor.validate_email(email)
    
    def convert_classes_list_to_string(self) -> str:
        
        return ','.join(self.__classes)
    
    @staticmethod
    def validate_shift(shift: str) -> str:
        
        options = ['M', 'T']
        
        if shift.upper() in options:
            return shift
        
        shift = input('Por favor, insira um turno válido! ').upper()
        return Instructor.validate_shift(shift)
    