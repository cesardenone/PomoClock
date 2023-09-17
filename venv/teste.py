import pyodbc
import datetime

SERVER = 'DESKTOP-3R9MF7L'
DATABASE = 'POMOCLOCK'
USERNAME = 'SA'
PASSWORD = 'SuperPassword@182'

connectionString  = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
print("Conexão bem sucedida!")

hora_atual = datetime.datetime.now()

sql_query = f"""INSERT INTO ATIVIDADES(HORA_INICIO) VALUES ('{hora_atual}')"""

cursor = conn.cursor()
cursor.execute(sql_query)
cursor.commit()
