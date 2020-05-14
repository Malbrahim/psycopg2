import psycopg2

conn = psycopg2.connect('dbname=todoapp_psycopg2')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")
cur.execute('DROP TABLE IF EXISTS table2;')

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cur.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')


cur.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cur.execute(SQL, data)

cur.execute('INSERT INTO table2 (id, completed) VALUES (3, True)')

cur.execute('SELECT * FROM table2;')

fetchone = cur.fetchone()
fetchmany = cur.fetchmany(2)
fetchall = cur.fetchall()

print('fetchone : ', fetchone)
print('fetchmany 2 : ', fetchmany)
print('fetchall : ', fetchall)

# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()