import sqlite3


banco = sqlite3.connect('banco_apae.db')
cursor = banco.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contribuintes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT
    )
""")

banco.commit()
banco.close()