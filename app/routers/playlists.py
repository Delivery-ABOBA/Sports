from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.database import crud
from app.dependencies import get_db
from app.funcs.utils import get_jwt_sub

router = APIRouter(prefix="/playlists", tags=["Playlists"])


@router.get("/")
async def get_playlist_songs(request: Request, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.get_playlist_songs(user_id, db)


@router.patch("/add-track/{id}")
async def add_track_to_playlist(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.add_track_to_playlist(id, user_id, db)


@router.delete("/remove-track/{id}")
async def remove_track_from_playlist(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.remove_track_from_playlist(id, user_id, db)


@router.get("/favorites")
async def get_favorites(request: Request, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.get_favorites_by_user(user_id, db)


@router.post("/album/{id}")
async def add_album_to_favs(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.add_album_to_favs(id, user_id, db)


@router.post("/artist/{id}")
async def add_artist_to_favs(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.add_artist_to_favs(id, user_id, db)


@router.delete("/album/{id}")
async def remove_album_to_favs(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.remove_album_to_favs(id, user_id, db)


@router.delete("/artist/{id}")
async def remove_artist_to_favs(request: Request, id: int, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    return await crud.remove_artist_to_favs(id, user_id, db)
