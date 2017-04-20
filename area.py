import sqlite3

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()

query = "SELECT SUM(area_land) FROM facts WHERE area_land != ''";
result = cursor.execute(query).fetchone()
total_area_land = result[0]

query = "SELECT SUM(area_water) FROM facts WHERE area_water != ''";
result = cursor.execute(query).fetchone()
total_area_water = result[0]

ratio_land_to_water = total_area_land / total_area_water
print(ratio_land_to_water)