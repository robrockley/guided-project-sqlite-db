import sqlite3
import pandas as pd
import math

def final_population(df):
    initial_population = df["population"]
    growth_rate = df["population_growth"]
    
    t = 35 # set time to 35 years
    r = growth_rate / 100 # growth rate
    
    final_population = initial_population * (math.e ** (r * t))
    return final_population
    
conn = sqlite3.connect("factbook.db")
query = "select * from facts;"

facts = pd.read_sql_query(query, conn)
facts = facts.dropna(axis=0)
facts = facts[facts["area_land"] != 0]

facts["population_in_2050"] = facts.apply(final_population, axis=1)
facts = facts.sort_values(by='population_in_2050', ascending=False)
print(facts["name"][0:10])
    
    