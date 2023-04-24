from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import crud
from app.dependencies import get_db

router = APIRouter(prefix="/songs", tags=["Songs"])


@router.get("/random")
async def get_random_songs(db: Session = Depends(get_db)):
    return await crud.get_random_songs(db)


@router.get("/image/{id}")
async def get_image(id: int, db: Session = Depends(get_db)):
    data = await crud.get_file(id, db)
    return FileResponse(f"app/storage/{data.type}/{data.name}")


@router.get("/search/{type}/{name}")
async def search(type: int, name: str, db: Session = Depends(get_db)):
    return await crud.search(type, name, db)


@router.get("/{song_id}")
async def get_song(song_id: int, db: Session = Depends(get_db)):
    return FileResponse(f"app/storage/tracks/{(await crud.get_song(song_id, db)).file}")
