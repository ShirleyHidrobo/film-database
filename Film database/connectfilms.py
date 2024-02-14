import sqlite3 as sql

dbCon = sql.connect("python/python project/filmflix.db")

dbCursor = dbCon.cursor()