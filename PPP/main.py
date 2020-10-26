import psycopg2

print("Hola a todos")

conn = psycopg2.connect("host=163.178.107.7 dbname=b61976_aplicada user=laboratorios password=saucr.120")
cur = conn.cursor()
cur.execute("INSERT INTO aplicada.clientes (cedula, nombre, apellido_uno, apellido_dos, fecha_ins) VALUES ('305090411', 'Faubricio', 'Chaves', 'Hern.', '29/03/1998')")
conn.commit()
