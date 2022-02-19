import random
from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, generate_uuid

users = []


def random_time():
    random_hour = random.uniform(1, 2.5)
    given_time = datetime.utcnow()
    new_time = given_time + timedelta(hours=random_hour)

    return new_time


for index in range(0, 2):
    user = User(id=generate_uuid(), created=random_time(),
                email=f'email{index}@email.com')
    users.append(user)
    print(f'User: {user.email} has been created at {user.created}')


session_maker = sessionmaker(bind=create_engine("sqlite:///models.db"))

with session_maker() as session:
    for user in users:
        session.add(user)
        print(f'The following user was added to db:')
        print(user.dict())
    session.commit()


# with session_maker() as session:
#     users = session.query(User).all()
#     for user in users:
#         print(user.dict())
