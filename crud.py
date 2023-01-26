#  Crud operation methods
from sqlalchemy.orm import Session

import model
import schema


def get_all(db: Session):
    print("fetching records")
    return db.query(model.Movies).all()


def get_by_id(db: Session, sl_id: int):
    print("fetching record id={}".format(sl_id))
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()


def add(db: Session, movie: schema.MovieAdd):
    mv_details = model.Movies(
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        director=movie.director,
        geners=movie.geners,
        membership_required=movie.membership_required,
        cast=movie.cast,
        streaming_platform=movie.streaming_platform)
    print("saving new record")
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Movies(**movie.dict())


def delete(db: Session, sl_id: int):
    try:
        print("deleting record id={}".format(sl_id))
        db.query(model.Movies).filter(model.Movies.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


def update(db: Session, sl_id: int, details: schema.UpdateMovie):
    print("updating record id={}".format(sl_id))
    db.query(model.Movies).filter(model.Movies.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Movies).filter(model.Movies.id == sl_id).first()

