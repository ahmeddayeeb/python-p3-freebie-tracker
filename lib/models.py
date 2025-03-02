from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(dev=dev, item_name=item_name, value=value, company=self)
        return freebie

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False

    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship('Dev', backref='freebies')
    company = relationship('Company', backref='freebies')

    def __repr__(self):
        return f'<Freebie {self.item_name}>'

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'

Company.devs = relationship("Dev", secondary="freebies", backref="companies")
