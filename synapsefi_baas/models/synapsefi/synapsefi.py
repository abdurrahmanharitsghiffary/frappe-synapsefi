from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional


class SelfLink(BaseModel):
    href: HttpUrl


class Links(BaseModel):
    self: SelfLink


class Client(BaseModel):
    id: str
    name: str


class Login(BaseModel):
    email: EmailStr
    scope: str


class Extra(BaseModel):
    cip_tag: int
    date_joined: int
    extra_security: bool
    is_business: bool
    is_trusted: bool
    last_updated: int
    public_note: Optional[str]
    supp_id: Optional[str]


class SynapseResponse(BaseModel):
    error_code: str
    http_code: str
    limit: int
    page: int
    page_count: int
    success: bool
