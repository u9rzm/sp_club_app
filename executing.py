from postgres_class import w_db as db

contracts = '''DROP TABLE Contracts;
CREATE TABLE Contracts
(id serial PRIMARY KEY, Fname varchar NOT NULL,
Lname varchar NOT NULL,
tel integer,
end_date date NOT NULL);
'''


Anketa =  '''DROP TABLE Anketa;
CREATE TABLE Anketa
(id integer PRIMARY KEY, weight varchar,
height varchar,
FOREIGN KEY (id) REFERENCES Users (id) ON DELETE SET NULL); 
'''
vizit=  '''
CREATE TABLE Vizits
(start_time timestamp PRIMARY KEY, Contract_id integer, end_time timestamp,
FOREIGN KEY (Contract_id) REFERENCES Contracts (id) ON DELETE CASCADE); 
'''



Users =  '''DROP TABLE Users;
CREATE TABLE Users (id varchar PRIMARY KEY, pass varchar NOT NULL,

Anketa_id integer UNIQUE,
Contract_id integer,
FOREIGN KEY (Contract_id) REFERENCES Contracts (id) ON DELETE SET NULL);
'''
tabs = [Anketa]
for i in tabs:
    a=db()
    b=a.exec(i)
	



