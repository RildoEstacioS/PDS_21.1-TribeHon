import psycopg2
conn = psycopg2.connect("dbname=test user=postgres password=Horrivel/10")
cur = conn.cursor()
print('foi')
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
print('era para ter criado')
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("SELECT * FROM test WHERE num = 0;")

print(cur.fetchone())
conn.commit()
cur.close()
conn.close()
'''conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()'''

