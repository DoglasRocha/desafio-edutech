import re
from program_messenger import ProgramMessenger
from errors import (InvalidNameError, InvalidEmailError, 
                    InvalidClassError, InvalidCGMError,
                    InvalidShiftError, InvalidStatusError,
                    InvalidTeacherNameError)

class Student:
    
    def __init__(self, name: str, email: str, _class: str, CGM: str,
                 shift: str, status: str, teacher: str) -> None:
        self.__name = Student.__validate_name(name)
        self.__email = Student.__validate_email(email)
        self.__class = Student.__validate_class(_class)
        self.__CGM = Student.__validate_CGM(CGM)
        self.__shift = Student.__validate_shift(shift)
        self.__status = Student.__validate_status(status)
        self.__teacher = Student.__validate_teacher(teacher)
        
        self.send_to_database()
        
    def send_to_database(self) -> None:
        ProgramMessenger.insert_student_into_database(self.__name,
                                                      self.__email,
                                                      self.__class,
                                                      self.__CGM,
                                                      self.__shift,
                                                      self.__status,
                                                      self.__teacher)
    
    @staticmethod
    def __validate_name(name: str) -> str:
        
        pattern = re.compile('[a-zA-Z ]{1,}')
        
        if pattern.match(name):
            return name
        
        raise InvalidNameError()
    
    @staticmethod
    def __validate_email(email: str) -> str:
        
        pattern = re.compile('[a-z.]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        raise InvalidEmailError()
    
    @staticmethod
    def __validate_class(class_: str) -> str:
        
        pattern = re.compile('[0-9]{6,}')
        
        if pattern.match(class_):
            return class_
        
        raise InvalidClassError()
    
    @staticmethod
    def __validate_CGM(CGM: str) -> str:
        
        pattern = re.compile('[0-9]{8,}')
        
        if pattern.match(CGM):
            return CGM
        
        raise InvalidCGMError()
    
    @staticmethod
    def __validate_status(status: str) -> bool:
        
        options = ['ATIVO', 'INATIVO']
        
        if status.upper() in options:
            return status
        
        raise InvalidStatusError()
    
    @staticmethod
    def __validate_shift(shift: str) -> str:
        
        options = ['M', 'T']
        
        if shift.upper() in options:
            return shift
        
        raise InvalidShiftError()
    
    @staticmethod
    def __validate_teacher(teacher: str) -> str:
        
        pattern = re.compile('[a-zA-Z ]{1,}')
        teachers = ProgramMessenger.select_all_teacher_names()
        
        for teacher_name in teachers:
            if (pattern.match(teacher) and teacher in teacher_name):
                return teachers
        
        raise InvalidTeacherNameError()
        
        
    