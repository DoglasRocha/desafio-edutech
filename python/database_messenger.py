from cursor import connect_to_database

def execute_query(query: str):
    cursor = connect_to_database()
        
    cursor.execute(query)
    cursor.close()