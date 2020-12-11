class Entity_db:
    entity ={'contracts': {'id': 'serial PRIMARY KEY',' Fname': 'varchar NOT NULL','Lname': 'varchar NOT NULL','tel': 'integer','end_date': 'date NOT NULL'}, 'Anketa': {'id': 'integer PRIMARY KEY', 'weight': 'varchar','height': 'varchar'}, 'vizits': {'start_time': 'timestamp PRIMARY KEY', 'Contract_id': 'integer', 'end_time': 'timestamp'}, 'Users':{'id': 'varchar PRIMARY KEY', 'pass': 'varchar NOT NULL', 'Anketa_id': 'integer', 'Contract_id': 'integer'}, 'meloman':{'id':'integer', 'anketa_id':'integer', 'genre':'integer'}, 'genre':{'id':'integer', 'name':'varchar'}}

    
