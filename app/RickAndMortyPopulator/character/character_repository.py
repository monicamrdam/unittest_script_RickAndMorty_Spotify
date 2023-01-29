import random
import string
import sqlite3 as sql

class CharacterRepository:
    def __init__(self):
        pass

    @staticmethod
    def get_db():
        DATABASE_URI='../app/db_RAndM_Spotify.db'
        conn = sql.connect(DATABASE_URI)
        return conn

    @staticmethod
    def create_tables():
        # Las tablas son una lista de sentencias
        tables = [
            """CREATE TABLE IF NOT EXISTS characters(
            uuid TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            list_episode TEXT NOT NULL)""",
        ]
        db = CharacterRepository.get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)

    @staticmethod
    def get_uuid(num_dig):
        uuid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_dig))
        return uuid

    @staticmethod
    def insert_character(uuid, name, location, list_episode):
        db = CharacterRepository.get_db()
        cursor = db.cursor()
        statement = "INSERT INTO characters (uuid, name, location,list_episode) VALUES (?,?,?,?)"
        cursor.execute(statement, [uuid, name, location, list_episode])
        db.commit()