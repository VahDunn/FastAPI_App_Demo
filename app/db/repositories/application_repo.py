from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.application_model import Application


class ApplicationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_application(self, user_name: str, description: str) -> Application:
        new_application = Application(user_name=user_name, description=description)
        self.db.add(new_application)
        await self.db.commit()
        await self.db.refresh(new_application)
        return new_application

    async def get_applications(self, user_name: str = None, skip: int = 0, limit: int = 10):
        query = select(Application)
        if user_name:
            query = query.filter(Application.user_name == user_name)
        result = await self.db.execute(query.offset(skip).limit(limit))
        return result.scalars().all()