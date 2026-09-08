from sqlalchemy.orm import Session
import models
import schemas
from utils import generate_short_code

def create_short_url(db: Session, url_data: schemas.URLCreate):
    short_code = generate_short_code()
    db_url = models.URL(
        short_code=short_code,
        original_url=url_data.original_url
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

def increment_clicks(db: Session, url: models.URL):
    url.clicks += 1
    db.commit()
    db.refresh(url)
    return url