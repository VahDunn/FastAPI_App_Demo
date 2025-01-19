import pytest
from unittest.mock import Mock, AsyncMock
from datetime import datetime
from app.schemas.application import ApplicationResponse, ApplicationCreate
from app.api.endpoints.applications import create_application, get_applications_list


# Фикстуры для тестов
@pytest.fixture
def mock_application_repo(mocker):
    mock = AsyncMock()
    mocker.patch('app.db.repositories.application_repo.ApplicationRepository', return_value=mock)
    return mock


@pytest.fixture
def mock_kafka_producer(mocker):
    mock = AsyncMock()
    mocker.patch('app.core.app.app.producer.send_and_wait', return_value=mock)
    return mock


@pytest.fixture
def mock_db():
    return AsyncMock()


# Тесты
@pytest.mark.asyncio
async def test_create_application(mock_application_repo, mock_kafka_producer, mock_db):
    # Подготовка тестовых данных
    test_date = datetime(2024, 3, 21, 12, 0, 0)
    mock_application_repo.create_application.return_value = ApplicationResponse(
        id=1,
        user_name="Test Application",
        description="Test Description",
        created_at=test_date
    )

    application_data = ApplicationCreate(
        user_name="Test Application",
        description="Test Description"
    )

    # Выполнение тестируемой функции
    response = await create_application(application_data, mock_db)

    # Проверки
    mock_application_repo.create_application.assert_called_once_with(
        "Test Application",
        "Test Description"
    )

    mock_kafka_producer.assert_called_once_with(
        'applications',  # Предполагается, что это значение из settings.KAFKA_TOPIC
        value={
            'id': 1,
            'user_name': "Test Application",
            'description': "Test Description",
            'created_at': str(test_date)
        }
    )

    assert response.id == 1
    assert response.user_name == "Test Application"
    assert response.description == "Test Description"
    assert response.created_at == test_date


@pytest.mark.asyncio
async def test_get_applications_list_without_filters(mock_application_repo, mock_db):
    # Подготовка тестовых данных
    test_date = datetime(2024, 3, 21, 12, 0, 0)
    mock_application_repo.get_applications.return_value = [
        ApplicationResponse(
            id=1,
            user_name="Test Application 1",
            description="Test Description 1",
            created_at=test_date
        ),
        ApplicationResponse(
            id=2,
            user_name="Test Application 2",
            description="Test Description 2",
            created_at=test_date
        )
    ]

    # Выполнение тестируемой функции
    response = await get_applications_list(user_name=None, page=1, size=10, db=mock_db)

    # Проверки
    mock_application_repo.get_applications.assert_called_once_with(None, 0, 10)

    assert len(response) == 2
    assert response[0].id == 1
    assert response[0].user_name == "Test Application 1"
    assert response[1].id == 2
    assert response[1].user_name == "Test Application 2"


@pytest.mark.asyncio
async def test_get_applications_list_with_username_filter(mock_application_repo, mock_db):
    # Подготовка тестовых данных
    test_date = datetime(2024, 3, 21, 12, 0, 0)
    mock_application_repo.get_applications.return_value = [
        ApplicationResponse(
            id=1,
            user_name="Test User",
            description="Test Description",
            created_at=test_date
        )
    ]

    # Выполнение тестируемой функции
    response = await get_applications_list(user_name="Test User", page=1, size=10, db=mock_db)

    # Проверки
    mock_application_repo.get_applications.assert_called_once_with("Test User", 0, 10)

    assert len(response) == 1
    assert response[0].user_name == "Test User"


@pytest.mark.asyncio
async def test_get_applications_list_pagination(mock_application_repo, mock_db):
    # Подготовка тестовых данных
    test_date = datetime(2024, 3, 21, 12, 0, 0)
    mock_application_repo.get_applications.return_value = [
        ApplicationResponse(
            id=3,
            user_name="Test Application 3",
            description="Test Description 3",
            created_at=test_date
        )
    ]

    # Выполнение тестируемой функции
    response = await get_applications_list(user_name=None, page=2, size=2, db=mock_db)

    # Проверки
    mock_application_repo.get_applications.assert_called_once_with(None, 2, 2)

    assert len(response) == 1
    assert response[0].id == 3