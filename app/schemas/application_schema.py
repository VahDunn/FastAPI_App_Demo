from pydantic import BaseModel, Field

class ApplicationCreate(BaseModel):
    user_name: str = Field(
        ...,
        description="Имя пользователя",
        min_length=1,
        max_length=50,
    )
    description: str = Field(
        ...,
        description="Описание заявки",
        min_length=1,
        max_length=500,
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "user_name": "Ilyas_Apunov",
                    "description": "This is a description of the application.",
                }
            ]
        }


class ApplicationResponse(BaseModel):
    id: int
    user_name: str
    description: str
    created_at: str

    class Config:
        from_attributes = True