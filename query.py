import sqlite3

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()

query = "select name from facts order by population ASC limit 10";
result = cursor.execute(query).fetchall()
print(result)
