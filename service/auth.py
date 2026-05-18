from datetime import datetime as dt, timedelta
from jose import jwt
from dataclasses import dataclass
from exception import UserNotFoundException, UserNotCorrectPasswordException
from models import UserProfile
from repository import UserRepository
from schema import UserLoginSchema
from settings import Settings


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException()
        if user.password != password:
            raise UserNotCorrectPasswordException

    def generate_access_token(self, user_id: str):
        expires_date_unix = (dt.utcnow() + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {"user_id": user_id, "expire": expires_date_unix},
            self.settings.JWT_SECRET_KEY,
            algorithm=self.settings.JWT_ENCODE_ALGORITHM
        )
        return token
