from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/courier", response_model=schemas.Courier)
def create_courier(courier: schemas.CourierCreate, db: Session = Depends(get_db)):
    return crud.create_courier(db=db, courier=courier)


@app.get("/courier", response_model=List[schemas.Courier])
def get_couriers(db: Session = Depends(get_db)):
    return crud.get_couriers(db)


@app.get("/courier/{courier_id}", response_model=schemas.Courier)
def get_courier(courier_id: int, db: Session = Depends(get_db)):
    return crud.get_courier(db, courier_id)


@app.post("/order", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@app.get("/order/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get_order(db, order_id)


@app.post("/order/{order_id}", response_model=schemas.Order)
def complete_order(order_id: int, db: Session = Depends(get_db)):
    return crud.complete_order(db, order_id)
