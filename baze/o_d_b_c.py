# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import pyodbc
# https://www.postgresql.org/ftp/odbc/versions/msi/
# C:\Windows\ODBCINST.INI


class PCCPathsDatabase:
    def __init__(self):
        self.conn = pyodbc.connect(
            p_str=None,
            driver="PostgreSQL Unicode(x64)",
            server="11.214.2.139",
            port=5433,
            database="pcc_paths",
            uid="pcc_user",
            pwd="pcc1234",
        )


if __name__ == '__main__':
    db = PCCPathsDatabase()

    print(db.conn.execute("SELECT 1;").fetchone())
