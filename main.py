import locale
import Entity_db
import pandas as pd
import postgres_class as pg

contracts=pd.read_excel('contracts.xlsx')
contracts['date'] = contracts1['end_date'].apply(str)
contracts.drop('end_date', axis=1, inplace=True)
contracts.rename(columns={'date':'end_date'}, inplace=True)
for i in contracts.values:
    pg.ins('contracts',dict(zip((contracts.keys()),i)))