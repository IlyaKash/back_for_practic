from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class CourierBase(BaseModel):
    name: str
    districts: List[str]


class CourierCreate(CourierBase):
    pass


class Courier(CourierBase):
    id: int
    active_order: Optional[dict]
    avg_order_complete_time: Optional[datetime]
    avg_day_orders: Optional[int]

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    name: str
    district: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    courier_id: Optional[int]
    status: int

    class Config:
        orm_mode = True
