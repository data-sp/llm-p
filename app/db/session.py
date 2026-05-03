from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings

sqlite_url = f"sqlite+aiosqlite:///{settings.sqlite_path}"

engine = create_async_engine(sqlite_url, echo=False, future=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
