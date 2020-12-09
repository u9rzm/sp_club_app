class Entiti_db:

    _cont =['contracts',{'id': 'serial PRIMARY KEY',' Fname': 'varchar NOT NULL','Lname': 'varchar NOT NULL','tel': 'integer','end_date': 'date NOT NULL'}]

    _ank =  ['Anketa', {'id': 'integer PRIMARY KEY', 'weight': 'varchar',
'height': 'varchar'}, 'FOREIGN KEY (id) REFERENCES Users (id) ON DELETE SET NULL']

    _viz= ['vizits', {'start_time': 'timestamp PRIMARY KEY', 'Contract_id': 'integer', 'end_time': 'timestamp'},'FOREIGN KEY (Contract_id) REFERENCES Contracts (id) ON DELETE CASCADE']

    _use = ['Users',{'id': 'varchar PRIMARY KEY', 'pass': 'varchar NOT NULL', 'Anketa_id': 'integer', 'Contract_id': 'integer'}, 'FOREIGN KEY (Contract_id) REFERENCES Contracts (id) ON DELETE SET NULL)']

    def _init_(self, table):
        
        print('Таблицы - _cont ',self._cont[0],', _ank ',self._ank[0], ', _viz ',self._viz[0], ', _use ',self._use[0])
       # print(cont[1].keys() ,',\n ', ank[1].keys() , ',\n ', viz[1].keys() , ',\n ', list(use[1].keys() ))
