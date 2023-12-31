"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follow, Like

db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follow, DictReader(follows))

like1 = Like(
    user_id=1,
    message_id=897
)
like2 = Like(
    user_id=2,
    message_id=63
)
like3 = Like(
    user_id=3,
    message_id=439
)

db.session.add_all([like1, like2, like3])

db.session.commit()
