import difflib
#import json
#from pathlib import Path
import sqlite3
d={}

with sqlite3.connect("dictionary.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dictionary")
    for row in cursor:
     d=dict(cursor)

#data = Path("data.json").read_text()
#dictionary = json.loads(data)
def search(word):
    if word in d.keys():
        return d[word]
    elif difflib.get_close_matches(word, d.keys()) == []:
        return ('Your word does not exist!')
    else:
        return ( f'Your correct word is between {difflib.get_close_matches(word,d.keys())}')


