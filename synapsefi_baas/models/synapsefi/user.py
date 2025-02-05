from pydantic import BaseModel, EmailStr
from typing import List, Any, Optional
from .synapsefi import Links, Client, Extra, Login, SynapseResponse


class User(BaseModel):
    _id: str
    _links: Links
    account_closure_date: Optional[str]
    client: Client
    documents: List[Any]
    emails: List[EmailStr]
    extra: Extra
    flag: str
    flag_code: Optional[str]
    is_hidden: bool
    legal_names: List[str]
    logins: List[Login]
    permission: str
    permission_code: Optional[str]
    phone_numbers: List[str]
    photos: List[Any]
    refresh_token: str
    watchlists: str


class SynapseUserListResponse(SynapseResponse):
    users: List[User]
    users_count: int
