from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean

from app.database.database import DataBase


class Users(DataBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(90), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    username = Column(String(150))
    image = Column(Integer, ForeignKey("images.id"))


class Images(DataBase):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    type = Column(String(90))
    name = Column(String(300))


class PlaylistSongs(DataBase):
    __tablename__ = "playlist_songs"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    song_id = Column(Integer, ForeignKey("songs.id"), primary_key=True)


class Favorites(DataBase):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    album_id = Column(Integer, ForeignKey("albums.id"))
    artist_id = Column(Integer, ForeignKey("users.id"))


class Albums(DataBase):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    artist = Column(Integer, ForeignKey("users.id"))
    image = Column(Integer, ForeignKey("images.id"))
    description = Column(String(300))


class Songs(DataBase):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    album = Column(Integer, ForeignKey("albums.id"))
    name = Column(String(300))
    duration = Column(String(30))
    file = Column(String(300))
    image = Column(Integer, ForeignKey("images.id"))
