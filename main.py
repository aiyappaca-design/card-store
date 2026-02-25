from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Card
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

class CardCreate(BaseModel):
    id: str
    status: str
    transaction_type: str
    transaction_limit: float
    currency: str


class CardResponse(BaseModel):
    id: str
    status: str
    transaction_type: str
    transaction_limit: float
    currency: str

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cards", response_model=CardResponse)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    new_card = Card(**card.dict())
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card


@app.get("/cards/{card_id}", response_model=CardResponse)
def get_card(card_id: str, db: Session = Depends(get_db)):
    card = db.query(Card).filter(Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@app.get("/")
def root():
    return {"message": "Card Store Service Running"}