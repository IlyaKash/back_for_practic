from sqlalchemy.orm import Session
import models
import schemas


def create_courier(db: Session, courier: schemas.CourierCreate):
    db_courier = models.Courier(name=courier.name)
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier


def get_couriers(db: Session):
    return db.query(models.Courier).all()


def get_courier(db: Session, courier_id: int):
    return db.query(models.Courier).filter(models.Courier.id == courier_id).first()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def complete_order(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order.status != 1:
        return None  # Order already completed or not found
    db_order.status = 2  # Set status to completed
    db.commit()
    return db_order
