from fastapi.testclient import TestClient
from main import app
from database import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# override db session to use separate database for tests
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[override_get_db] = override_get_db


def test_create_courier():
    client = TestClient(app)
    response = client.post(
        "/courier",
        json={"name": "John Doe", "districts": ["District A", "District B"]},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_get_couriers():
    client = TestClient(app)
    response = client.get("/courier")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_order():
    client = TestClient(app)
    response = client.post(
        "/order", json={"name": "Order 1", "district": "District A"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Order 1"


def test_get_order():
    client = TestClient(app)
    response = client.get("/order/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Order 1"
