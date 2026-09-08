from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import engine, get_db
import crud, schemas, models
import webbrowser
import threading
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

@app.get("/")
def home():
    return {"message": "URL Shortener is running!", "docs": "/docs"}

@app.post("/shorten")
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db, url_data)
    return {
        "short_code": db_url.short_code,
        "original_url": db_url.original_url,
        "short_url": f"http://localhost:8000/{db_url.short_code}",
        "clicks": db_url.clicks,
        "created_at": db_url.created_at
    }

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_code(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    crud.increment_clicks(db, db_url)
    return RedirectResponse(url=db_url.original_url)

@app.get("/stats/{short_code}")
def get_stats(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_code(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {
        "short_code": db_url.short_code,
        "original_url": db_url.original_url,
        "clicks": db_url.clicks,
        "created_at": db_url.created_at
    }

def open_browser():
    time.sleep(2)
    webbrowser.open("http://localhost:8000/docs")

if __name__ == "__main__":
    import uvicorn
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)