from sqlalchemy import Column, Integer, String, Date,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(Date,default=datetime.now)
    updated_at = Column(Date,default=datetime.now, onupdate=datetime.now)
    playlists = relationship("Playlist", back_populates="user")

class PlatFormIntegrations(Base):
    __tablename__ = "platform_integrations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    platform_id = Column(Integer, ForeignKey("platform.id"))
    access_token = Column(String, index=True)
    refresh_token = Column(String)
    created_at = Column(Date, default=datetime.now)
    updated_at = Column(Date, default=datetime.now, onupdate=datetime.now)
    owner = relationship("Platform", back_populates="platforms")


class Platform(Base):
    __tablename__ = "platform"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    platform_name = Column(String, index=True)
    client_id = Column(String)
    client_secret = Column(String)
    created_at = Column(Date, default=datetime.now)
    updated_at = Column(Date, default=datetime.now, onupdate=datetime.now)
    platforms = relationship("PlatFormIntegrations", back_populates="owner")  # Back-populates to PlatFormIntegrations
    playlists = relationship("Playlist", back_populates="platform")  # Back-populates to Playlist


class Playlist(Base):
    __tablename__ = "playlist"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    playlist_name = Column(String, index=True)
    platform_id = Column(Integer, ForeignKey("platform.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    playlist_id = Column(String, index=True)
    created_at = Column(Date, default=datetime.now)
    updated_at = Column(Date, default=datetime.now, onupdate=datetime.now)
    user = relationship("User", back_populates="playlists")
    platform = relationship("Platform", back_populates="playlists")  