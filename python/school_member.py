from abc import ABCMeta
from errors import (InvalidNameError, InvalidEmailError,
                    InvalidShiftError)
import re

class SchoolMember(metaclass=ABCMeta):
    
    @staticmethod
    def validate_name(name: str) -> str:
        
        pattern = re.compile('[a-zA-Z ]{1,}')
        
        if pattern.match(name):
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
    