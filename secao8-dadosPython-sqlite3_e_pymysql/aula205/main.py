import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas linhas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

# cursor.execute(sql, ['Renan Garcia', 9.9])
# cursor.executemany(
#     sql,
#     [
#         ['Renan', 9.9], ['Thaís', 13.8]  # Também podem ser tuplas
#     ]
# )
# cursor.execute(sql, {'nome': 'Renan Garcia', 'peso': 9.9})
cursor.executemany(
    sql,
    (
        {'nome': 'Renan Garcia', 'peso': 9.9},
        {'nome': 'Thaís Andrade', 'peso': 13.8},
        {'nome': 'Aurora', 'peso': 10.9},
        {'nome': 'Pedro', 'peso': 15.9},
    )
)
connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)
