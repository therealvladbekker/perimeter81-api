from dataclasses import dataclass
from typing import List, Dict, Any
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
    order: SortOrder


@dataclass()
class ApiCallResultBase:
    success: bool
    errors: List[Err]


@dataclass
class CreateGroupApiCallResult(ApiCallResultBase):
    results: List[CreateGroupResponse]


@dataclass
class CreateUserApiCallResult(ApiCallResultBase):
    results: List[CreateUserResponse]


@dataclass
class ListUsersArguments:
    q: str
    sort: List[Sort]
    qType: QueryType  # = QueryType.full.full
    qOperator: QueryOperator  # = QueryOperator.or_
    page: int = 1
    limit: int = 50


@dataclass
class NetworkGeoPoint:
    latitude: float
    longitude: float


@dataclass
class NetworkProvider:
    region: str
    continentCode: str
    countryCode: str


@dataclass
class NetworkRegion:
    geoPoint: NetworkGeoPoint
    name: str
    instances: List[Dict]
    provider: NetworkProvider
    id: str


@dataclass
class NetworkMeta:
    networkId: str
    instanceId: str


@dataclass
class NetworkStatus:
    type_: str
    meta: NetworkMeta
    status: bool


@dataclass
class NetworkHealth:
    health: List[NetworkStatus]


@dataclass
class Network:
    geoPoint: NetworkGeoPoint
    name: str
    isDefault: bool
    regions: List[NetworkRegion]
    id: str


@dataclass
class ListNetworksApiCallResult(ApiCallResultBase):
    results: List[Network]


@dataclass
class GetNetworksHealthApiCallResult(ApiCallResultBase):
    results: List[NetworkHealth]
