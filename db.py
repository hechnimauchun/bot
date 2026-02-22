import sqlite3
from config import db
conn = sqlite3.connect(db, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER NOT NULL UNIQUE,
	"ism"	TEXT NOT NULL,
	"familiya"	TEXT NOT NULL,
    "tel_nomer" NUMERIC NOT NULL,
	"lokatsiya"	TEXT NOT NULL,
	PRIMARY KEY("user_id")
);""")
conn.commit()