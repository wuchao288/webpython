from pymssql import connect 
conn = connect(host=".", user="sa", password="123", database="test")
cursor = conn.cursor()
cursor.execute("select * from stu")
rows = cursor.fetchall()
for row in rows:
    print(row[0])
    print(row[1])
