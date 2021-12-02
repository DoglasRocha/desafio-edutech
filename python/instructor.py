import re
from program_messenger import ProgramMessenger
from school_member import SchoolMember
from errors import InvalidClassesError

class Instructor(SchoolMember):
    
    def __init__(self, name: str, email: str, classes: str, 
                 shift: str) -> None:
        self.__name = Instructor.validate_name(name, False)
        self.__email = Instructor.validate_email(email)
        self.__classes = Instructor.__validate_classes(classes)
        self.__shift = Instructor.validate_shift(shift)
        
    def send_to_database(self) -> None:
        ProgramMessenger.insert_teacher_into_database(self.__name,
                                                      self.__email,
                                                      self.__classes,
                                                      self.__shift)
        
    @staticmethod
    def __validate_classes(classes: str) -> str:
        
        pattern = re.compile('[0-9]{6,}')
        classes_list = classes.split(',')
        
        for class_ in classes_list:
            if not pattern.match(class_):
                raise InvalidClassesError()
            
        return classes
    
