from logging import exception

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from ...db.models.application_model import Application
from ...db.repositories.application_repo import ApplicationRepository
from app.core.app import app
from ...core.config import settings
from ...schemas.application_schema import ApplicationCreate, ApplicationResponse
from ...core.database import get_db
from ...utils.logger import LOG




application_router = APIRouter()


@application_router.post("/", response_model=ApplicationResponse)
async def create_application(
        application_data: ApplicationCreate,
        db: AsyncSession = Depends(get_db)
):
    repo = ApplicationRepository(db)
    application = await repo.create_application(application_data.user_name, application_data.description)
    LOG.info(f"New application with id {application.id} for user {application.user_name}\
     was created at {application.created_at}")
    LOG.info(f"Application description: {application.description}")

    message = {
        "id": application.id,
        "user_name": application.user_name,
        "description": application.description,
        "created_at": str(application.created_at)
    }
    await app.producer.send_and_wait(settings.KAFKA_TOPIC, value=message)

    return ApplicationResponse(id=application.id,
                               user_name=application.user_name,
                               description=application.description,
                               created_at=str(application.created_at))


@application_router.get("/")
async def get_applications_list(
        user_name: str | None = Query(None),
        page: int = Query(1, gt=0),
        size: int = Query(10, gt=0),
        db: AsyncSession = Depends(get_db)
):
    try:
        skip = (page - 1) * size
        repo = ApplicationRepository(db)
        applications = await repo.get_applications(user_name, skip, size)
        LOG.info(f"Retrieved {len(applications)} applications for query: user_name={user_name}, page={page}, size={size}")
        return applications
    except Exception as e:
        LOG.info("Something happened")
        LOG.error(f"{str(e)}")