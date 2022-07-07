from sqlalchemy import select, update, delete, insert

# SQL ALCHEMY CRUD OPERATIONS

def select_all(session, table):
    return session.query(table).all()

def update_one(session, table, id, data):
    session.query(table).filter(table.id == id).update(data)
    session.commit()

def delete_one(session, table, id):
    session.query(table).filter(table.id == id).delete()
    session.commit()

def insert_one(session, table, data):
    session.add(data)
    session.commit()
    return data.id

