from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    avg_order_complete_time = Column(DateTime)
    avg_day_orders = Column(Integer)

    orders = relationship("Order", back_populates="courier")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    district = Column(String)
    status = Column(Integer, default=1)
    courier_id = Column(Integer, ForeignKey("couriers.id"))

    courier = relationship("Courier", back_populates="orders")
