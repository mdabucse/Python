import sqlite3


class Database:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = sqlite3.connect("orm.db")
            cls._connection.row_factory = sqlite3.Row
        return cls._connection

    @classmethod
    def execute(cls, query, params=None):
        conn = cls.connect()
        cursor = conn.cursor()

        if params is None:
            params = []

        print(f"SQL: {query}")

        cursor.execute(query, params)
        conn.commit()

        return cursor

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.execute(query, params)
        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.execute(query, params)
        row = cursor.fetchone()

        return dict(row) if row else None