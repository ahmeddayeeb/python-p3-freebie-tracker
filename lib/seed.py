#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    company1 = Company(name='Google', founding_year=1998)
    company2 = Company(name='Facebook', founding_year=2004)
    dev1 = Dev(name='John')
    dev2 = Dev(name='Jane')
    session.add_all([company1, company2, dev1, dev2])
    session.commit()
    freebie1 = company1.give_freebie(dev1, 'T-shirt', 10)
    freebie2 = company2.give_freebie(dev2, 'Sticker', 1)
    session.add_all([freebie1, freebie2])
    session.commit()

    print(freebie1.print_details())
    print(Company.oldest_company())
    print(dev1.received_one('T-shirt'))
    print(dev2.received_one('T-shirt'))
    dev1.give_away(dev2, freebie1)
    print(freebie1.dev)
