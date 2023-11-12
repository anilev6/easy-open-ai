from fastapi import APIRouter

router = APIRouter()


class Depends:
    pass


def get_db():
    pass


class Session:
    pass


class User:
    pass


def get_current_user(user: User) -> str:
    return User.name


class ResponseContact:
    pass


@router.get("/")
async def list_contacts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    current_user: User = Depends(get_current_user()),
) -> list[ResponseContact] | ResponseContact:
    return 1
