from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.database import crud
from app.dependencies import get_db
from app.funcs.utils import get_jwt_sub

router = APIRouter(prefix="/artists", tags=["Artists"])


@router.get("/random")
async def get_random_artist(db: Session = Depends(get_db)):
    return await crud.get_random_artist(db)


@router.get("/albums")
async def get_artist_albums(request: Request, artist_id: Optional[int] = None, db: Session = Depends(get_db)):
    user_id = get_jwt_sub(request)['id']
    if artist_id is None:
        artist_id = user_id
    return await crud.get_artist_albums(artist_id, user_id, db)
