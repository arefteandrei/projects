from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///books.db', echo=True)
meta = MetaData()

books = Table(
    'books', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('year', String),
)

meta.create_all(engine)
conn = engine.connect()
conn.execute(books.insert(),
[
    {'id': 1, 'title': 'Corabii astrale', 'year': 1950},
    {'id': 2, 'title': 'Drum pintre astrii', 'year': 1954},
    {'id': 3, 'title': 'Cutia Pandorei', 'year': 1986},
    {'id': 4, 'title': 'Templul Paradit', 'year': 1989},
])

b = books.select()
data = conn.execute(b).fetchall()

for i in data:
    print(f'id : {i[0]}')
    print(f'title : {i[1]}')
    print(f'year : {i[2]}')