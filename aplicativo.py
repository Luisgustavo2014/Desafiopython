# Main class
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# Initializing the app
app = FastAPI(title="CRUD Operations using Python FastAPI")


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all movies
@app.get('/get-all', response_model=List[schema.Movie])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db=db)


# Save new movie
@app.post('/add', response_model=schema.MovieAdd)
def add(movie: schema.MovieAdd, db: Session = Depends(get_db)):
    movie_id = crud.get_by_id(db=db, sl_id=movie.movie_id)
    if movie_id:
        print("Resource conflict")
        raise HTTPException(status_code=409, detail=f"Resource id {movie_id} already exist")

    return crud.add(db=db, movie=movie)


# Delete a movie by id
@app.delete('/delete')
def delete(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_by_id(db=db, sl_id=sl_id)
    if not details:
        print("Entity not found")
        raise HTTPException(status_code=404, detail=f"Resource not found")
    try:
        crud.delete(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")

    return {"status": "accepted", "code": "202", "message": "Resource deleted"}


# Update a movie by id
@app.put('/update', response_model=schema.Movie)
def update(sl_id: int, update_param: schema.UpdateMovie, db: Session = Depends(get_db)):
    details = crud.get_by_id(db=db, sl_id=sl_id)
    if not details:
        print("Entity not found")
        raise HTTPException(status_code=404, detail=f"Resource not found")

    return crud.update(db=db, details=update_param, sl_id=sl_id)


# Driver code
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=7001, log_level="debug")
