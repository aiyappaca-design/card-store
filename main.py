from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Card

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cards")
def create_card(card: dict, db: Session = Depends(get_db)):
    new_card = Card(**card)
    db.add(new_card)
    db.commit()
    return {"message": "Card created"}

@app.get("/cards/{card_id}")
def get_card(card_id: str, db: Session = Depends(get_db)):
    card = db.query(Card).filter(Card.id == card_id).first()
    return card