from dbCfg import *
import psycopg2 as pg
import traceback
import utils.logs as logger


class Psql:
    def __init__(self):
        self.conn: Psql.Connection = Psql.Connection()
        self.cursor = self.conn.getCursor()

    def newTable(self, name: str, cursor):
        return self.Table(cursor, name)

    class Table:
        def __init__(self, cursor, name: str):
            self.name_: str = name
            self.cursor_: pg.cursor = cursor

        def returnAll(self, prop: str | None = None, propWhere: str | None = None) -> list:
            try:
                if prop is None and propWhere is None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
                if prop is None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
                if prop is not None and propWhere is None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
                if prop is not None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
                return self.cursor_.fetchall()
            except Exception as ex:
                trace = traceback.format_exc()
                logger.crit(trace)
                return []

        def returnMany(self, size: int, propWhere: str | None = None, prop: str | None = None) -> list:
            try:
                if prop is None and propWhere is None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
                if prop is None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
                if prop is not None and propWhere is None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
                if prop is not None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
                return self.cursor_.fetchmany(size=size)

            except Exception as ex:
                trace = traceback.format_exc()
                logger.crit(trace)
                return []

        def returnOne(self, propWhere: str | None = None, prop: str | None = None) -> list:
            try:
                if prop is None and propWhere is None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_}""")
                if prop is None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT * FROM {self.name_} WHERE {propWhere}""")
                if prop is not None and propWhere is None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_}""")
                if prop is not None and propWhere is not None:
                    self.cursor_.execute(f"""SELECT {prop} FROM {self.name_} WHERE {propWhere}""")
                return self.cursor_.fetchone()
            except Exception as ex:
                trace = traceback.format_exc()
                logger.crit(trace)
                return []

        def insert(self, rows: str, args: str) -> bool:

            try:
                self.cursor_.execute(f"""INSERT INTO {self.name_} ({rows}) VALUES """ + args)
                return True
            except Exception as ex:
                trace = traceback.format_exc()
                logger.crit(trace)
                return False

        def update(self, setters: str, equals: str, whers: str = None) -> bool:
            try:
                if whers is None:
                    self.cursor_.execute(f"""UPDATE {self.name_} SET {setters} = {equals}""")
                    return True
                self.cursor_.execute(f"""UPDATE {self.name_} SET {setters} = {equals} WHERE {whers}""")
                return True
            except Exception as ex:
                trace = traceback.format_exc()
                logger.crit(trace)
                return False

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


db = Psql()
