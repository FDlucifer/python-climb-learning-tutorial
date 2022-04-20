# pip install pydantic

import string
import json
import pydantic
from typing import Optional

class User(pydantic.BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str]
    phone_number: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_phone_or_mail(cls, values):
        if "email" in values or "phone_number" in values:
            return values
        else:
            raise ValueError("need either email or phone_number")

    @pydantic.validator("username")
    @classmethod
    def username_valid(cls, value):
        if any(p in value for p in string.punctuation):
            raise ValueError("username must not include punctuation")
        else:
            return value

    @pydantic.validator("password")
    @classmethod
    def password_valid(cls, value):
        if len(value) < 8:
            raise ValueError("password must be at least 8 characters long")
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):
                        return value
        raise ValueError("password needs at least one punctuation symbol, digit, upper and lower")

    @pydantic.validator("age", "score")
    @classmethod
    def number_valid(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Numbers must be positive")

user1 = User(username="user1", password="123casjdUCD.",
            age=20, score=0, email="luci@qq.com")

print(user1)
print(user1.age)

json_users = [User(**u) for u in json.load(open("users.json"))]
print(json_users)