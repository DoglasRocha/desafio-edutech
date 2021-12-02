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
    
    @staticmethod
    def select_all_teachers() -> list:
        
        query = 'SELECT * FROM Professores'
        
        response = execute_query(query).fetchall()
        return response
    
    @staticmethod
    def select_students_by_name(name: str) -> list:
        
        query = f'''SELECT Nome, Email, CGM, Turma FROM Alunos 
        WHERE Nome LIKE '%{name}%'
        '''
        
        response = execute_query(query).fetchall()
        return response
    
    @staticmethod
    def select_student(student_name: str) -> list:
        
        query = f"SELECT * FROM Alunos WHERE Nome = '{student_name}'"
        
        response = execute_query(query).fetchall()
        return response
    
    @staticmethod
    def update_student(name: str, email: str, class_: str, CGM: str,
                       shift: str, status: str, teacher: str) -> None:
        
        query = f'''UPDATE Alunos
        SET Email = '{email}',
            Turma = '{class_}'
            CGM = {CGM}
            Turno = '{shift}'
            Status_ = '{status}'
            Professor = '{teacher}'
        WHERE Nome = '{name}'
        '''
        
        execute_query(query)
        
    @staticmethod
    def select_teacher(name: str) -> list:
        
        query = f'''SELECT Nome, Email, Turno FROM Professores 
        WHERE Nome LIKE '%{name}%'
        '''
        
        response = execute_query(query).fetchall()
        return response        
    
    @staticmethod
    def select_students_per_teacher(teacher_name: str) -> list:
        
        query = f'''SELECT Nome, Email, CGM, Turno, Turma, Professor
        FROM Alunos
        WHERE Professor = '{teacher_name}'
        '''
        
        response = execute_query(query).fetchall()
        return response