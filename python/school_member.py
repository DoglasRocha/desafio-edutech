from abc import ABCMeta
from errors import (ExistentStudentError, ExistentTeacherError, InvalidNameError, InvalidEmailError,
                    InvalidShiftError)
from program_messenger import ProgramMessenger
import re

class SchoolMember(metaclass=ABCMeta):
    
    @staticmethod
    def validate_name(name: str, student: bool) -> str:
        
        pattern = re.compile('[a-zA-Z ]{1,}')
        
        if pattern.match(name):
            
            if student:
                result = ProgramMessenger.select_student(name)
                
                if len(result) > 0:
                    raise ExistentStudentError()
            
            else:
                result = ProgramMessenger.select_teacher(name)
                
                if len(result) > 0:
                    raise ExistentTeacherError()
                
            return name
        
        raise InvalidNameError()
    
    @staticmethod
    def validate_email(email: str) -> str:
        
        pattern = re.compile('[a-z.]{0,}@escola.pr.gov.br')
        
        if pattern.match(email):
            return email
    
        raise InvalidEmailError()
    
    @staticmethod
    def validate_shift(shift: str) -> str:
        
        options = ['M', 'T']
        
        if shift.upper() in options:
            return shift
        
        raise InvalidShiftError()
    