from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str = None
    name: str = None
    picture: str = None
    total_chip: int = None


class SlotSession(BaseModel):
    bet: int = None
    result: List = []
    change: int = None




class ChannelBase(BaseModel):
    email: str = None
    name: str = None
    avatar: str = None
    type: str = None
    avatar_thumb: str = None
    is_active: bool = False
    member_ids: List = []
    last_message: dict = None
    last_message_time: datetime = None
    friend_id: str = None


class ParticipantBase(BaseModel):
    role: str
    last_read: Optional[datetime]


class MemberAdd(BaseModel):
    ids: List[str]


class CreateMesage(BaseModel):
    type: str
    content: str


class MessageTypeCreate(BaseModel):
    name: str
    key: str


class MessageCreateSchema(BaseModel):
    id: Optional[str]
    type_id: Optional[str]
    sender_id: str
    channel_id: str
    content: str
    status: str
    visible: bool = True
    created: Optional[str]
    modified: Optional[str]


class ChannelCreate(BaseModel):
    participant_ids: List[str]
    message: CreateMesage
    avatar: Optional[str]
    name: str


class ChannelUpdate(BaseModel):
    avatar: Optional[str]
    name: str


class ChannelSchema(ChannelBase):
    id: Optional[str]
    owner_id: Optional[str]

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    id: str = None
    avatar: str = None
    avatar_thumb: str = None
    display_name: str = None

    class Config:
        orm_mode = True


class Participant(ParticipantBase):
    id: str
    user_id: str
    channel_id: str

    class Config:
        orm_mode = True


class EmitChannelSchema(BaseModel):
    avatar: Optional[str]
    name: str


class ParticipantMember(ParticipantBase):
    id: str
    role: str
    user: UserCreateSchema

    class Config:
        orm_mode = True


class CreateChannelMessage(BaseModel):
    message: CreateMesage
    channel_id: str


class UpdateMessage(BaseModel):
    content: str
