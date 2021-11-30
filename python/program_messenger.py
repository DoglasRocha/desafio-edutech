from database_messenger import execute_query

class ProgramMessenger:
    
    @staticmethod
    def insert_student_into_database(name: str, email: str, 
                                     class_: str, CGM: str,
                                     shift: str, status: str,
                                     teacher: str) -> None:
        query = f'''INSERT Alunos
            VALUES (
                '{name}', '{email}', '{class_}', {CGM}, 
                '{shift}', '{status}', '{teacher}'
            )'''
            
        execute_query(query)
        
    @staticmethod
    def insert_teacher_into_database(name: str, email: str,
                                     classes: str, shift: str):
        query = f'''INSERT Professores
            VALUES (
                '{name}', '{email}', '{classes}', '{shift}'
            )'''
            
        execute_query(query)
        
    @staticmethod
    def select_all_teacher_names() -> list:
        
        query = 'SELECT Nome FROM Professores'
        
        response = execute_query(query).fetchall()
        return response
    
    @staticmethod
    def select_all_students() -> list:
        
        query = 'SELECT * FROM Alunos'
        
        response = execute_query(query).fetchall()
        return response