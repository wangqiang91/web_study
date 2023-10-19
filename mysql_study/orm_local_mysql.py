from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Boolean
engine = create_engine('mysql://root:123456@localhost:3306/school')
base = declarative_base()

class News(base):
    __tablename__ = 'news'
    id = Column(Integer,premary_key=True)
    title = Column(String(50),nullable=False)
    content = Column(String(5000),nullable=False)
    created_at= Column(DateTime,nullable=False)
    type = Column(String(10),nullable=False)
    image = Column(String(300),nullable=False)
    author = Column(String(20),nullable=False)
    view_count = Column(Integer,nullable=False)
    is_valid = Column(Boolean,nullable=False)
