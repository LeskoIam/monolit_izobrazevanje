# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = "dokreg"
db_password = "dokreg"
db_database = "dokreg"
SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@localhost:5432/{database}".format(user=db_user,
                                                                                            password=db_password,
                                                                                            database=db_database)
# ################################################################################################################

Base = declarative_base()


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_on = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    active = Column(Boolean, nullable=False, default=True)
    active_revision = Column(Integer, nullable=False)
    under_edit = Column(Boolean, nullable=False, default=False)


# ################################################################################################################

class DBHelper:

    def __init__(self, ip=None, port=None, database=None, user=None, password=None):

        self.ip = ip
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        self.engine = None
        self.Session = None
        self.session = None
        self.connected = False

    def connect(self):
        """
        Creates new session for db.
        """
        # self.engine = create_engine("mssql://{self.user}:{self.password}@{self.ip}:{self.port}/{self.database}".format(self=self),
        #                             echo=False)

        # self.engine = create_engine("postgresql://{user}:{password}@localhost:5432/{database}".format(user=db_user,
        #                                                                                               password=db_password,
        #                                                                                               database=db_database))

        self.engine = create_engine("sqlite:///orm_in_detail.sqlite".format(self=self), echo=False)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.connected = True

    def disconnect(self):
        """
        Closes session.
        """
        try:
            self.session.close()
            self.session = None
            self.connected = False
        except AttributeError:
            print("Can't close connection that is not opened.")

    def execute_sql(self, sql, return_list=False):
        """Execute supplied SQL string.

        :param sql: SQL string to be executed
        :param return_list: If True result will be returned as list otherwise as object
        :return: Result of the query
        """
        if not self.connected:
            self.connect()
        data = self.session.execute(sql)
        if return_list:
            out = []
            for line in data:
                out.append([str(x) for x in line])
            return out
        return data


if __name__ == '__main__':
    db = DBHelper()
    db.connect()

    Base.metadata.create_all(db.engine)

    # #################################

    d = Document(title="Test Title", active=True, active_revision=1)
    d1 = Document(title="Test Title1", active=True, active_revision=1)
    db.session.add(d)

    db.session.flush()
    print(d.id)

    db.session.add(d1)
    db.session.flush()
    print(d1.id)

    db.session.commit()

    print(db.session.query(Document).filter(Document.id == 1).all())

    result = db.execute_sql("""
    SELECT * FROM document as d;
    
    """)

    print(result)

    for row in result:
        print(row.title)


    doc = db.session.query(Document).filter(Document.id == 1).one()
    print(doc)

    doc.title = "popravek"

    db.session.add(doc)
    db.session.commit()

    # result_update = db.execute_sql("""
    # UPDATE document SET title = 'trymeagain' WHERE id = 1;
    #
    # """, return_list=True)
    # print(result_update)


    db.disconnect()
