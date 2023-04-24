from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.database import crud, schemas
from app.dependencies import get_db
from app.funcs.utils import get_jwt_sub

router = APIRouter(prefix="/albums", tags=["Albums"])


@router.get("/random")
async def get_random_albums(db: Session = Depends(get_db)):
    return await crud.get_random_album(db)


@router.get("/get/{id}")
async def get_album_songs(id: int, db: Session = Depends(get_db)):
    return await crud.get_album_songs(id, db)


@router.get("/{id}/songs")
async def get_album_songs(id: int, db: Session = Depends(get_db)):
    return await crud.get_album_songs(id, db)


@router.post("/create/{name}/{description}")
async def create_album(request: Request, name: str, description: str, data: schemas.AlbumData = Depends(schemas.AlbumData.form), db: Session = Depends(get_db)):
    data.artist = get_jwt_sub(request)['id']
    data.name = name
    data.description = description
    return await crud.create_album(data, db)


@router.post("/add-track/{album}/{name}")
async def add_track_to_album(album: int, name: str, request: Request,
                             data: schemas.SongData = Depends(schemas.SongData.form),
                             db: Session = Depends(get_db)):
    data.artist = get_jwt_sub(request)['id']
    data.name = name
    data.album = album
    print(data)
    return await crud.add_track_to_album(data, db)


@router.delete("/remove-track/{id}")
async def remove_track_from_album(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.remove_track_from_album(id, user_id, db)


@router.delete("/delete/{id}")
async def delete_album(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.remove_album(id, user_id, db)
