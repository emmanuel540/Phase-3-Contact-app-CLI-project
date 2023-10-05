

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    contacts = relationship('Contact', back_populates='category')

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    notes = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='contacts')
    communication_history = relationship('CommunicationHistory', back_populates='contact')

class CommunicationHistory(Base):
    __tablename__ = 'communication_history'

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    date = Column(DateTime, default=datetime.now)
    communication_type = Column(String)
    notes = Column(String)

    contact = relationship('Contact', back_populates='communication_history')
