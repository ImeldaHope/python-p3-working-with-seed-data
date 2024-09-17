#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    #clear table game every time we seed to avoid duplicates. NB: Be careful with this since it empties the table
    session.query(Game).delete()
    session.commit()

    # Add a console message so we can see output when the seed file runs
print("Seeding games...")

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )

for _ in range(50)]

session.bulk_save_objects(games)
session.commit()