from dataclasses import dataclass
from typing import NamedTuple, List, Dict, Any
from enum import Enum, auto

Err = str
Auth = Dict


@dataclass
class Group:
    name: str
    description: str


@dataclass
class CreateGroupResponse:
    tenantId: str
    name: str
    description: str
    isDefault: bool
    applications: List
    networks: List
    vpnLocations: List
    users: List
    createdAt: str
    updatedAt: str
    id: str


@dataclass
class ProfileData:
    firstName: str
    lastName: str
    roleName: str
    phone: str


@dataclass
class User:
    email: str
    inviteMessage: str
    accessGroups: List[str]
    profileData: ProfileData


@dataclass
class InternalUser(User):
    idpType: str = 'database'
    origin: str = 'API'
    emailVerified: bool = True


@dataclass
class CreateUserResponse:
    tenantId: str
    terminated: bool
    initialsColor: str
    invitationAttempts: int
    role: str
    username: str
    emailVerified: bool
    inviteMessage: str
    roleName: str
    firstName: str
    lastName: str
    phone: str
    initials: str
    idProviders: Any
    createdAt: str
    updatedAt: str
    id: str


class QueryType(Enum):
    full: auto()
    partial: auto()


class QueryOperator(Enum):
    and_: auto()
    or_: auto()


class SortOrder(Enum):
    asc: auto()
    desc: auto


@dataclass
class Sort:
    field: str
    order: SortOrder = SortOrder.asc


class ApiCallResultBase(NamedTuple):
    success: bool
    errors: List[Err]


class CreateGroupApiCallResult(ApiCallResultBase):
    results: List[CreateGroupResponse]


class CreateUserApiCallResult(ApiCallResultBase):
    results: List[CreateUserResponse]


@dataclass
class ListUsersArguments:
    q: str
    sort: List[Sort]
    page: int = 1
    limit: int = 50
    qType: QueryType = QueryType.full
    qOperator: QueryOperator = QueryOperator.or_

# "tenantId":<TENANT_ID>,
# "terminated":false,
# "initialsColor":"#E46086",
# "invitationAttempts":0,
# "invitationToken":"<INVITATION_TOKEN>",
# "role":"NaHaEa8ayL",
# "username":"<USER_EMAIL>",
# "email":"<USER_EMAIL>",
# "emailVerified":true,
# "inviteMessage":"<INVITE_TEXT>",
# "roleName":"<PROFILE_ROLE>",
# "firstName":"<FIRST_NAME>",
# "lastName":"<LAST_NAME>",
# "phone":"<PHONE>",
# "initials":"DT",
# "idProviders":{
#   "database":{
#     "userId":null
#   }
# },
# "createdAt":"2021-09-29T13:59:56.694Z",
# "updatedAt":"2021-09-29T13:59:56.694Z",
# "id":"eZHoeJR2Y5"
