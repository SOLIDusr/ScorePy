from dbCfg import *
import psycopg2 as pg


class Psql:
    def __init__(self):
        self.conn: Psql.Connection = Psql.Connection()
        self.cursor: pg.cursor = self.conn.getCursor()

    def newTable(self, name: str, cursor):
        return self.Table(cursor, name)

    class Table:
        def __init__(self, cursor, name: str):
            self.name_: str = name
            self.cursor_: pg.cursor = cursor

        def returnAll(self, prop: str | None = None, propWhere: str | None = None) -> list | Exception:
            if prop is None and propWhere is None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
            if prop is None and propWhere is not None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
            if prop is not None and propWhere is None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
            if prop is not None and propWhere is not None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
            return self.cursor_.fetchall()

        def returnMany(self, size: int, propWhere: str | None = None, prop: str | None = None) -> list | Exception:
            if prop is None and propWhere is None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
            if prop is None and propWhere is not None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
            if prop is not None and propWhere is None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
            if prop is not None and propWhere is not None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
            return self.cursor_.fetchmany(size=size)

        def returnOne(self, propWhere: str | None = None, prop: str | None = None) -> list | Exception:
            if prop is None and propWhere is None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
            if prop is None and propWhere is not None:
                self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
            if prop is not None and propWhere is None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
            if prop is not None and propWhere is not None:
                self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
            return self.cursor_.fetchone()

        def insert(self,rows: str ,*args):
            self.cursor_.execute(f"""INSERT INTO {self.name_} ({rows}) VALUES ({args})""")
            return None

        def update(self, setters: str, equals: str, whers: str = None):
            if whers is None:
                self.cursor_.execute(f"""UPDATE {self.name_} SET {setters} = {equals}""")
                return None
            self.cursor_.execute(f"""UPDATE {self.name_} SET {setters} = {equals} WHERE {whers}""")
            return None

    class Connection:
        def __init__(
                self,
                host_: str = host,
                port_: str = port,
                userName_: str = userName,
                dbName_: str = dbName,
        ):
            super().__init__()
            self.userPass = input("Enter database password\n>")
            self.dataBase = pg.connect(
                host=host_,
                user=userName_,
                password=self.userPass,
                database=dbName_,
                port=port_,
            )

        def autocommit(self, state: bool = True) -> None:
            self.dataBase.autocommit = state

        def close(self):
            self.dataBase.close()

        def commit(self):
            self.dataBase.commit()

        def reset(self):
            self.dataBase.reset()

        def isClosed(self) -> int:
            return self.dataBase.closed

        def getCursor(self):
            return self.dataBase.cursor()
