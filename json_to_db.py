import sqlite3
import json
from pathlib import Path
data = Path("data.json").read_text()
dictionary = json.loads(data)
l1= list(dictionary.keys())
l2= list(dictionary.values())
str1= " "
i=0
a =  "INSERT INTO dictionary VALUES (?,?)" 
while i < len(l1):
    with sqlite3.connect("dictionary.db") as conn:
        cursor = conn.cursor()
        cursor.execute(a  ,  (l1[i],str1.join(l2[i]))  )
        i += 1  
conn.commit()
    

