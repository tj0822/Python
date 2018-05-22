from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+pypostgresql://sqlalchemy:sqlalchemy@localhost/sqlalchemy",
                       echo=True, convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db():
    import models
    metadata.create_all(bind=engine)