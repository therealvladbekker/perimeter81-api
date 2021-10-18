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


# ListNetworksApiCallResult(success=True, errors=None, results=[Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974),
#                                                                       name='ZZ Bad network   IP is WRONG', isDefault=False,
#                                                                       regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=34.789763, longitude=32.086789),
#                                                                                              name='Israel',
#                                                                                              instances=[{'tenantId': 'knowledgebase', 'network': 'EFfuLh4LqH', 'region': 'mya3cUVJ3a',
#                                                                                                          'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2020070600',
#                                                                                                          'resourceId': None, 'dns': 'knowledgebase-z5zuqo2qvp.pzero.perimeter81.com',
#                                                                                                          'ip': '212.59.64.68',
#                                                                                                          'tunnels': [{'tenantId': 'knowledgebase', 'network': 'EFfuLh4LqH', 'region':
#                                                                                                              'mya3cUVJ3a', 'instance': 'Z5ZUqO2QVP', 'interfaceName': 'Test', 'right':
#                                                                                                              '3.232.123.1', 'rightID': '3.232.123.1', 'keyExchange': 'ikev1',
#                                                                                                                       'phase1': {'auth': ['aes256'], 'encr': ['sha256'], 'dh': [14]}, 'phase2':
#                                                                                                                           {'auth': ['aes256'], 'encr': ['sha256'], 'dh': [14]},
#                                                                                                                       'passphrase': 'exU2Yuv4', 'leftSubnets': ['0.0.0.0/0'],
#                                                                                                                       'rightSubnets': ['10.0.0.0/12'], 'ikeLifeTime': '8h', 'lifetime': '1h',
#                                                                                                                       'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec',
#                                                                                                                       'createdAt': '2020-07-15T09:00:05.603Z',
#                                                                                                                       'updatedAt': '2020-07-15T09:00:05.604Z', 'id': '6jH5E9gAU8'}],
#                                                                                                          'createdAt': '2020-07-08T11:02:08.806Z', 'updatedAt': '2020-07-15T09:00:05.638Z',
#                                                                                                          'id': 'Z5ZUqO2QVP'}],
#                                                                                              provider=NetworkProvider(region='sx-il1', continentCode='AS', countryCode='IL'), id='mya3cUVJ3a')],
#                                                                       id='EFfuLh4LqH'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974),
#                                                                                                 name='AlexB-TestNetwork', isDefault=False,
#                                                                                                 regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=34.789763, longitude=32.086789),
#                                                                                                                        name='Israel', instances=[{'tenantId': 'knowledgebase', 'network': 'PBoeyZmYfg',
#                                                                                                                                                   'region': '8J25PfuCVC', 'instanceType': '2048',
#                                                                                                                                                   'imageType': 'sxp', 'imageVersion': 'sxp-2021091200',
#                                                                                                                                                   'resourceId': None, 'dns':
#                                                                                                                                                       'knowledgebase-vxale0malm.pzero.perimeter81.com', 'ip': '212.59.64.177', 'tunnels': [], 'createdAt': '2021-10-06T08:00:53.687Z', 'updatedAt': '2021-10-06T08:00:53.687Z', 'id': 'VxAle0MALM'}],
#                                                                                                                        provider=NetworkProvider(region='sx-il1', continentCode='AS', countryCode='IL'), id='8J25PfuCVC'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=8.644044, longitude=50.097352), name='Frankfurt 1',
#                                                                                                                                                                                                                                         instances=[{'tenantId': 'knowledgebase', 'network': 'PBoeyZmYfg', 'region': 'cWnCgFvYzg', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-no0bcmwcar.pzero.perimeter81.com', 'ip': '212.59.67.102', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'PBoeyZmYfg', 'region': 'cWnCgFvYzg', 'instance': 'no0Bcmwcar', 'interfaceName': 'WireGuardFra1', 'leftEndpoint': '3.70.46.157', 'leftAllowedIP': ['10.100.0.0/16', '10.200.0.0/16'], 'vault': 'saferx/data/nqzCRHHYx4/PBoeyZmYfg/cWnCgFvYzg/no0Bcmwcar/WireGuardFra1', 'requestConfigToken': 'NDRmZmUzNjYxOTlkY2M2MzBlNzFiODIzOTRjNGI0MGM3OTBjZjQ0NzhlYmU5NWJl', 'type': 'connector', 'createdAt': '2021-10-06T06:05:02.720Z', 'updatedAt': '2021-10-06T06:05:02.726Z', 'id': 'xB2aBYr6vX'}], 'createdAt': '2021-10-05T14:15:36.616Z', 'updatedAt': '2021-10-06T06:05:02.733Z', 'id': 'no0Bcmwcar'}], provider=NetworkProvider(region='sx-fr1', continentCode='EU', countryCode='DE'), id='cWnCgFvYzg')], id='PBoeyZmYfg'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Or Test', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=37.339625, longitude=-121.945058), name='Silicon Valley', instances=[{'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'omlk0h89mM', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021040400', 'resourceId': None, 'dns': 'knowledgebase-bjm9sjxx1a.pzero.perimeter81.com', 'ip': '131.226.33.221', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'omlk0h89mM', 'instance': 'BjM9sjXX1A', 'interfaceName': 'OVPN', 'passphrase': '$6$perimeter81$n4SW6D8KkvwA31PkuI6QTN6agHyo/QZa1y.xS6MWThB9XpK7kNwspXiWNcP5KV9JuuOkfXV/bjUjl6GaN3L9S/', 'username': 'vbnp08RSKsGZKZPJ', 'type': 'openvpn', 'createdAt': '2021-06-15T23:31:40.306Z', 'updatedAt': '2021-06-16T14:39:06.419Z', 'id': '7CTGfbWgi7'}, {'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'omlk0h89mM', 'instance': 'BjM9sjXX1A', 'interfaceName': 'AWSUSEast1', 'right': '23.20.20.156', 'rightID': '23.20.20.156', 'keyExchange': 'ikev2', 'phase1': {'dh': [21], 'encr': ['sha512'], 'auth': ['aes256']}, 'phase2': {'dh': [21], 'encr': ['sha512'], 'auth': ['aes256']}, 'passphrase': 'B8PKaHXzvY6oqvEfp4ZeTUCpOnjHV0W5', 'leftSubnets': ['0.0.0.0/0'], 'rightSubnets': ['0.0.0.0/0'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-07-18T09:44:44.325Z', 'updatedAt': '2021-08-25T17:43:18.222Z', 'id': 'epfL6SEPPy'}, {'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'omlk0h89mM', 'instance': 'BjM9sjXX1A', 'interfaceName': 'Ubuntu10athome', 'leftEndpoint': '0.0.0.0', 'leftAllowedIP': ['10.0.0.0/24'], 'vault': 'saferx/data/nqzCRHHYx4/sOroNGZxDK/omlk0h89mM/BjM9sjXX1A/Ubuntu10athome', 'requestConfigToken': 'YjFlZmJhMGM3ZDExN2MzNzg4MTdiYjFhNmU1Nzc5NTFmMTAxMmZlNzA1NjQ3YzRh', 'type': 'connector', 'createdAt': '2021-08-25T17:56:29.208Z', 'updatedAt': '2021-08-25T17:56:29.210Z', 'id': 'KDFKfZZ0rM'}, {'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'omlk0h89mM', 'instance': 'BjM9sjXX1A', 'interfaceName': 'ovpntest', 'passphrase': '$6$perimeter81$n7JuBV5JN.nIxsLLaNqMW5l86m4i6XdSmCt8nU3bzL4jc1L4Oa1MdEEkdreaXfFFs0u1kXzJ1RklLCc3PGeoy/', 'username': 'JSnTMECa7PSEUiZM', 'type': 'openvpn', 'createdAt': '2021-08-25T18:07:06.851Z', 'updatedAt': '2021-08-25T18:10:59.707Z', 'id': 'ngKZ2I4mev'}], 'createdAt': '2021-04-14T19:32:48.871Z', 'updatedAt': '2021-08-25T18:07:06.857Z', 'id': 'BjM9sjXX1A'}], provider=NetworkProvider(region='sx-sj1', continentCode='NA', countryCode='US'), id='omlk0h89mM'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=-46.6361, longitude=-23.5475), name='Sao Paulo', instances=[{'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'ujZTmFo7oQ', 'instanceType': '1x2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021082200', 'resourceId': None, 'dns': 'knowledgebase-w6r5xxcyz4.pzero.perimeter81.com', 'ip': '131.226.41.16', 'tunnels': [], 'createdAt': '2021-08-26T17:53:20.678Z', 'updatedAt': '2021-08-26T17:53:20.679Z', 'id': 'W6R5xXcyZ4'}], provider=NetworkProvider(region='br-sao1', continentCode='SA', countryCode='BR'), id='ujZTmFo7oQ'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=40.705564, longitude=-74.118429), name='New York', instances=[{'tenantId': 'knowledgebase', 'network': 'sOroNGZxDK', 'region': 'xp0PS5D3sQ', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-oyfpzepndd.pzero.perimeter81.com', 'ip': '131.226.37.140', 'tunnels': [], 'createdAt': '2021-09-17T17:29:39.172Z', 'updatedAt': '2021-09-17T17:29:39.172Z', 'id': 'oyfpzEpNDD'}], provider=NetworkProvider(region='sx-ny1', continentCode='NA', countryCode='US'), id='xp0PS5D3sQ')], id='sOroNGZxDK'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Yael Yevgeni Test', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=34.789763, longitude=32.086789), name='Israel', instances=[{'tenantId': 'knowledgebase', 'network': 'tsfBNpuAPw', 'region': 'O5bUtO8Mg7', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021040400', 'resourceId': None, 'dns': 'knowledgebase-h89pdpkzco.pzero.perimeter81.com', 'ip': '212.59.64.183', 'tunnels': [], 'createdAt': '2021-04-20T09:13:28.930Z', 'updatedAt': '2021-09-20T10:48:34.049Z', 'id': 'H89pdPKzCO'}, {'tenantId': 'knowledgebase', 'network': 'tsfBNpuAPw', 'region': 'O5bUtO8Mg7', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021040400', 'resourceId': None, 'dns': 'knowledgebase-ii1tacg5z1.pzero.perimeter81.com', 'ip': '212.59.64.187', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'tsfBNpuAPw', 'region': 'O5bUtO8Mg7', 'instance': 'Ii1tACG5z1', 'interfaceName': 'Test1', 'passphrase': '$6$perimeter81$PXJv5l5onO7U/QO/pDvPw/xU/WhAPlNhbdVdvXSnHYTqVvOCLu7OOXaHSiNd4PgACuy2z20QhSWEqu8F8wRuz0', 'username': 'JKhDgNK6JKBckIKv', 'type': 'openvpn', 'createdAt': '2021-09-20T10:46:30.190Z', 'updatedAt': '2021-09-20T10:46:30.191Z', 'id': 'ivjlw4OCE2'}], 'createdAt': '2021-04-20T09:13:28.946Z', 'updatedAt': '2021-09-20T10:46:30.196Z', 'id': 'Ii1tACG5z1'}], provider=NetworkProvider(region='sx-il1', continentCode='AS', countryCode='IL'), id='O5bUtO8Mg7')], id='tsfBNpuAPw'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Shalev', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=34.789763, longitude=32.086789), name='Israel', instances=[{'tenantId': 'knowledgebase', 'network': 'DEIHSodlwX', 'region': 'u37FG3EkKT', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021061200', 'resourceId': None, 'dns': 'knowledgebase-rzir3ukb8s.pzero.perimeter81.com', 'ip': '212.59.64.201', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'DEIHSodlwX', 'region': 'u37FG3EkKT', 'instance': 'RZir3UkB8s', 'interfaceName': 'otunnel', 'passphrase': '$6$perimeter81$w2nP7JxIOiBpQ3PvtaXZnMOWRt9ZcMpqfOpebwHh8NyGdvmvgyiI59w/bFHHPEA.pe2iJ32E9p/xQ8PmY.KEC/', 'username': 'YO0fhH2TlcUt56wx', 'type': 'openvpn', 'createdAt': '2021-07-05T15:59:15.455Z', 'updatedAt': '2021-07-05T15:59:15.456Z', 'id': 'nr11KvX6O8'}, {'tenantId': 'knowledgebase', 'network': 'DEIHSodlwX', 'region': 'u37FG3EkKT', 'instance': 'RZir3UkB8s', 'interfaceName': 'AWStunnel', 'right': '3.21.90.216', 'rightID': '3.21.90.216', 'keyExchange': 'ikev1', 'phase1': {'auth': ['aes128'], 'encr': ['sha1'], 'dh': [2]}, 'phase2': {'auth': ['aes128'], 'encr': ['sha1'], 'dh': [2]}, 'passphrase': 'NM7EcLxEQToe7Ru1gQqt5KPdBUtdHPrt', 'leftSubnets': ['10.249.0.0/16'], 'rightSubnets': ['172.16.100.0/24'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-07-06T13:49:23.111Z', 'updatedAt': '2021-07-06T13:49:23.112Z', 'id': 'lJlBufICWf'}], 'createdAt': '2021-06-17T10:31:35.578Z', 'updatedAt': '2021-10-14T13:50:10.221Z', 'id': 'RZir3UkB8s'}, {'tenantId': 'knowledgebase', 'network': 'DEIHSodlwX', 'region': 'u37FG3EkKT', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-4stxrmrety.pzero.perimeter81.com', 'ip': '212.59.64.82', 'tunnels': [], 'createdAt': '2021-10-14T13:45:55.247Z', 'updatedAt': '2021-10-14T13:45:55.248Z', 'id': '4STxRmrEty'}], provider=NetworkProvider(region='sx-il1', continentCode='AS', countryCode='IL'), id='u37FG3EkKT')], id='DEIHSodlwX'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Kyle Krisher Test', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=41.8781136, longitude=-87.6297982), name='Chicago 1', instances=[{'tenantId': 'knowledgebase', 'network': 'PpMJelHA1J', 'region': '861j0UW6Pt', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021061200', 'resourceId': None, 'dns': 'knowledgebase-iggja4gpqq.pzero.perimeter81.com', 'ip': '131.226.36.68', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'PpMJelHA1J', 'region': '861j0UW6Pt', 'instance': 'IGgja4gPQQ', 'interfaceName': 'pfSenseTest', 'right': '0.0.0.0', 'rightID': '18.118.63.95', 'keyExchange': 'ikev2', 'phase1': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'phase2': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'passphrase': 'wFx7OLRR', 'leftSubnets': ['10.244.0.0/16'], 'rightSubnets': ['0.0.0.0/0'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-06-23T18:25:35.574Z', 'updatedAt': '2021-07-01T14:20:57.481Z', 'id': 'RbuU72DN6t'}, {'tenantId': 'knowledgebase', 'network': 'PpMJelHA1J', 'region': '861j0UW6Pt', 'instance': 'IGgja4gPQQ', 'interfaceName': 'FortinetTest', 'right': '65.60.250.36', 'rightID': '65.60.250.36', 'keyExchange': 'ikev2', 'phase1': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'phase2': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'passphrase': 'tEspV6ml68XP87bWzx0oIxzdJ6', 'leftSubnets': ['0.0.0.0/0'], 'rightSubnets': ['192.168.1.0/24'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-07-30T12:34:40.992Z', 'updatedAt': '2021-07-30T13:00:54.617Z', 'id': '37Mo1Cn86u'}], 'createdAt': '2021-06-22T13:03:24.916Z', 'updatedAt': '2021-07-30T12:56:59.654Z', 'id': 'IGgja4gPQQ'}], provider=NetworkProvider(region='sx-ch1', continentCode='NA', countryCode='US'), id='861j0UW6Pt'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=-46.6361, longitude=-23.5475), name='Sao Paulo', instances=[{'tenantId': 'knowledgebase', 'network': 'PpMJelHA1J', 'region': 'bLhXxHuS8y', 'instanceType': '1x2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021081100', 'resourceId': None, 'dns': 'knowledgebase-j6gnk0o1hv.pzero.perimeter81.com', 'ip': '131.226.41.14', 'tunnels': [], 'createdAt': '2021-08-13T00:25:26.653Z', 'updatedAt': '2021-08-13T00:25:26.654Z', 'id': 'J6gnk0O1HV'}], provider=NetworkProvider(region='br-sao1', continentCode='SA', countryCode='BR'), id='bLhXxHuS8y'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=33.7489954, longitude=-84.3879824), name='Atlanta', instances=[{'tenantId': 'knowledgebase', 'network': 'PpMJelHA1J', 'region': 'eh66uTkb0p', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-q84gaealvc.pzero.perimeter81.com', 'ip': '155.138.223.174', 'tunnels': [], 'createdAt': '2021-09-16T14:52:34.875Z', 'updatedAt': '2021-09-16T14:52:34.876Z', 'id': 'q84GaEalvC'}], provider=NetworkProvider(region='ATL', continentCode='NA', countryCode='US'), id='eh66uTkb0p')], id='PpMJelHA1J'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='AlexZinkevychTest', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=33.7489954, longitude=-84.3879824), name='Atlanta', instances=[{'tenantId': 'knowledgebase', 'network': 'yGo8X6AG0g', 'region': 'xs9s24DKdy', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021061200', 'resourceId': None, 'dns': 'knowledgebase-8edrsjrfct.pzero.perimeter81.com', 'ip': '155.138.175.42', 'tunnels': [], 'createdAt': '2021-07-19T12:12:43.428Z', 'updatedAt': '2021-07-19T12:12:43.428Z', 'id': '8EDRsjRfct'}], provider=NetworkProvider(region='ATL', continentCode='NA', countryCode='US'), id='xs9s24DKdy')], id='yGo8X6AG0g'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Moshe Training', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=41.8781136, longitude=-87.6297982), name='Chicago 1', instances=[{'tenantId': 'knowledgebase', 'network': 'ps5hya8NTb', 'region': 'CuQsRg071F', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021081100', 'resourceId': None, 'dns': 'knowledgebase-1rekjxpdhg.pzero.perimeter81.com', 'ip': '131.226.36.87', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'ps5hya8NTb', 'region': 'CuQsRg071F', 'instance': '1REkJXpdHG', 'interfaceName': 'GCP1', 'right': '34.132.36.34', 'rightID': '34.132.36.34', 'keyExchange': 'ikev2', 'phase1': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'phase2': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'passphrase': 'Aa123456', 'leftSubnets': ['10.246.0.0/16'], 'rightSubnets': ['10.89.0.0/16'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-09-19T13:37:44.338Z', 'updatedAt': '2021-09-19T13:37:44.340Z', 'id': 'WfkAiok3u0'}], 'createdAt': '2021-08-15T05:33:05.930Z', 'updatedAt': '2021-10-10T14:46:39.435Z', 'id': '1REkJXpdHG'}], provider=NetworkProvider(region='sx-ch1', continentCode='NA', countryCode='US'), id='CuQsRg071F')], id='ps5hya8NTb'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Block Youtube', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=32.7766642, longitude=-96.7969878), name='Dallas', instances=[{'tenantId': 'knowledgebase', 'network': 'iEC2BpdTTV', 'region': 'acrkQIE0XX', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021081100', 'resourceId': None, 'dns': 'knowledgebase-olnw0uhbes.pzero.perimeter81.com', 'ip': '131.226.34.251', 'tunnels': [], 'createdAt': '2021-08-14T00:08:07.583Z', 'updatedAt': '2021-09-25T22:09:22.945Z', 'id': 'oLnW0UHBES'}], provider=NetworkProvider(region='sx-ds1', continentCode='NA', countryCode='US'), id='acrkQIE0XX'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=37.773972, longitude=-122.431297), name='San Francisco', instances=[], provider=NetworkProvider(region='sfo1', continentCode='NA', countryCode='US'), id='tw1DFtadBw')], id='iEC2BpdTTV'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Casey', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=25.7616798, longitude=-80.1917902), name='Miami', instances=[{'tenantId': 'knowledgebase', 'network': '21n2UMMjPs', 'region': 'aN75PwjbV0', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021081100', 'resourceId': None, 'dns': 'knowledgebase-yhor9gecci.pzero.perimeter81.com', 'ip': '45.32.172.13', 'tunnels': [{'tenantId': 'knowledgebase', 'network': '21n2UMMjPs', 'region': 'aN75PwjbV0', 'instance': 'yHoR9GECcI', 'interfaceName': 'AWSProd', 'right': '13.59.247.155', 'rightID': '13.59.247.155', 'keyExchange': 'ikev2', 'phase1': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'phase2': {'dh': [14], 'encr': ['sha256'], 'auth': ['aes256']}, 'passphrase': 'pWo1_okf6AISH10lnPCXwdC2m6YqiEo7', 'leftSubnets': ['0.0.0.0/0'], 'rightSubnets': ['0.0.0.0/0'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-08-17T19:31:17.704Z', 'updatedAt': '2021-09-21T15:24:20.242Z', 'id': 'Y5K50Glk4D'}, {'tenantId': 'knowledgebase', 'network': '21n2UMMjPs', 'region': 'aN75PwjbV0', 'instance': 'yHoR9GECcI', 'interfaceName': 'CaseyTGW', 'right': '18.216.130.39', 'rightID': '18.216.130.39', 'keyExchange': 'ikev1', 'phase1': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'phase2': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'passphrase': 'nmV72K6beyrXNdUxiRKIjrP1MWfaEaW1', 'leftSubnets': ['10.240.0.0/16'], 'rightSubnets': ['0.0.0.0/0'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-08-19T14:16:20.787Z', 'updatedAt': '2021-08-19T14:16:20.788Z', 'id': '6vhPIl4GGO'}, {'tenantId': 'knowledgebase', 'network': '21n2UMMjPs', 'region': 'aN75PwjbV0', 'instance': 'yHoR9GECcI', 'interfaceName': 'UbuntuH', 'leftEndpoint': '47.197.201.151', 'leftAllowedIP': ['192.168.1.0/24'], 'vault': 'saferx/data/nqzCRHHYx4/21n2UMMjPs/aN75PwjbV0/yHoR9GECcI/UbuntuH', 'requestConfigToken': 'NjE1YTYyYmVkNmZjNjM5ZGU3OTllODg3ZDFlM2U3YWI5ZTY3OTVkMzZhMzExNjEz', 'type': 'connector', 'createdAt': '2021-08-28T15:47:56.743Z', 'updatedAt': '2021-08-30T20:24:44.646Z', 'id': 'qDcB15fHCa'}], 'createdAt': '2021-08-17T13:10:10.465Z', 'updatedAt': '2021-10-04T13:11:56.342Z', 'id': 'yHoR9GECcI'}], provider=NetworkProvider(region='MIA', continentCode='NA', countryCode='US'), id='aN75PwjbV0'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=39.833851, longitude=-74.871826), name='New Jersey', instances=[{'tenantId': 'knowledgebase', 'network': '21n2UMMjPs', 'region': 'EPTZoqhpzu', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-vt5jxywsiy.pzero.perimeter81.com', 'ip': '149.28.36.219', 'tunnels': [], 'createdAt': '2021-10-18T14:40:26.048Z', 'updatedAt': '2021-10-18T14:40:26.049Z', 'id': 'vt5jXywSIy'}], provider=NetworkProvider(region='EWR', continentCode='NA', countryCode='US'), id='EPTZoqhpzu')], id='21n2UMMjPs'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Elis-Net', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=51.50853, longitude=-0.076132), name='London', instances=[], provider=NetworkProvider(region='sx-lo1', continentCode='EU', countryCode='GB'), id='0qdfVv2uVB')], id='0ZCk76N0lt'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Sandbox', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=39.745629, longitude=-104.994513), name='Denver 1', instances=[{'tenantId': 'knowledgebase', 'network': 'if3vQ0BkoY', 'region': 'FC0bNSfshy', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-ceibfpr1ei.pzero.perimeter81.com', 'ip': '131.226.35.64', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'if3vQ0BkoY', 'region': 'FC0bNSfshy', 'instance': 'CEibFpr1Ei', 'interfaceName': 'AndroidOS', 'passphrase': '$6$perimeter81$mHgnnwLvTj3MA6d4fAAIPzgvfwJoavZuK7GzrJs0qCByV0FJ2GA2/YGrP4rWyBdO7RQ1fRk4IxgnjcioEP5R./', 'username': 'oKEhSA44iKFdtuUW', 'type': 'openvpn', 'createdAt': '2021-10-12T21:42:49.955Z', 'updatedAt': '2021-10-12T21:42:49.955Z', 'id': 'WAyZiIUjzc'}, {'tenantId': 'knowledgebase', 'network': 'if3vQ0BkoY', 'region': 'FC0bNSfshy', 'instance': 'CEibFpr1Ei', 'interfaceName': 'Android102', 'passphrase': '$6$perimeter81$i6f07oxbHiZauo2DzREurBIqOCY8azI2uxp684xPBQKT7p5Ha8FL1vKGG5WClBYt2EHktX/PBlmykZX1P0Dlo0', 'username': 'zlLhcczL8emckFPJ', 'type': 'openvpn', 'createdAt': '2021-10-12T22:00:34.635Z', 'updatedAt': '2021-10-12T22:00:34.636Z', 'id': 'PDmoBjeTGq'}], 'createdAt': '2021-09-17T16:31:00.918Z', 'updatedAt': '2021-10-12T22:00:34.643Z', 'id': 'CEibFpr1Ei'}], provider=NetworkProvider(region='sx-den1', continentCode='NA', countryCode='US'), id='FC0bNSfshy')], id='if3vQ0BkoY'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Ofirs try', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=33.7489954, longitude=-84.3879824), name='Atlanta', instances=[{'tenantId': 'knowledgebase', 'network': 'ioyKXdHUgN', 'region': 'Xb2sPT8EW7', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-ktlsgu3xbi.pzero.perimeter81.com', 'ip': '155.138.215.77', 'tunnels': [], 'createdAt': '2021-09-26T09:10:25.191Z', 'updatedAt': '2021-09-26T09:10:25.192Z', 'id': 'KtLSgu3xBi'}], provider=NetworkProvider(region='ATL', continentCode='NA', countryCode='US'), id='Xb2sPT8EW7')], id='ioyKXdHUgN'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Edwardo', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=25.7616798, longitude=-80.1917902), name='Miami', instances=[{'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'X9QqJZG98J', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-fqsomr5k5t.pzero.perimeter81.com', 'ip': '45.63.107.22', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'X9QqJZG98J', 'instance': 'fqsOMr5k5T', 'interfaceName': 'AWSlabEdwardo', 'right': '13.58.52.31', 'rightID': '13.58.52.31', 'keyExchange': 'ikev2', 'phase1': {'auth': ['aes256'], 'encr': ['sha512'], 'dh': [21]}, 'phase2': {'auth': ['aes256'], 'encr': ['sha512'], 'dh': [21]}, 'passphrase': 'E3GGn6q70nJgmnASuYTNfu29RFpXucdG', 'leftSubnets': ['10.253.0.0/16'], 'rightSubnets': ['10.0.0.0/24'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-10-06T19:29:35.395Z', 'updatedAt': '2021-10-06T19:29:35.397Z', 'id': 'DiNIawzXBC'}, {'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'X9QqJZG98J', 'instance': 'fqsOMr5k5T', 'interfaceName': 'GCPlab', 'right': '34.138.228.26', 'rightID': '34.138.228.26', 'keyExchange': 'ikev2', 'phase1': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'phase2': {'auth': ['aes256'], 'encr': ['sha1'], 'dh': [2]}, 'passphrase': 'Welcome1', 'leftSubnets': ['10.253.0.0/16'], 'rightSubnets': ['10.142.0.0/20'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-10-13T14:55:07.837Z', 'updatedAt': '2021-10-13T14:55:07.838Z', 'id': 'TcGv4wKVJk'}], 'createdAt': '2021-10-06T17:02:13.942Z', 'updatedAt': '2021-10-13T14:55:07.842Z', 'id': 'fqsOMr5k5T'}], provider=NetworkProvider(region='MIA', continentCode='NA', countryCode='US'), id='X9QqJZG98J'), NetworkRegion(geoPoint=NetworkGeoPoint(latitude=-46.6361, longitude=-23.5475), name='Sao Paulo', instances=[{'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'GtgzcTkuH2', 'instanceType': '1x2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-dbvh6dcob7.pzero.perimeter81.com', 'ip': '131.226.41.22', 'tunnels': [{'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'GtgzcTkuH2', 'instance': 'DbVh6dcOb7', 'interfaceName': 'AzureWG', 'leftEndpoint': '20.106.233.113', 'leftAllowedIP': ['10.150.0.0/24', '10.150.1.0/24'], 'vault': 'saferx/data/nqzCRHHYx4/ZnpZRW9d9J/GtgzcTkuH2/DbVh6dcOb7/AzureWG', 'requestConfigToken': 'YjgxYmEwYjdmMzY4M2ZiMzRlNTBiZjM1OGU3YTJhOTIxNmY3YzI3ODkzZTQ1ZjU5', 'type': 'connector', 'createdAt': '2021-10-07T18:28:21.490Z', 'updatedAt': '2021-10-07T23:09:27.409Z', 'id': 'iC9OJsYXKa'}, {'tenantId': 'knowledgebase', 'network': 'ZnpZRW9d9J', 'region': 'GtgzcTkuH2', 'instance': 'DbVh6dcOb7', 'interfaceName': 'AWSTransitGW', 'right': '3.18.0.161', 'rightID': '3.18.0.161', 'keyExchange': 'ikev1', 'phase1': {'dh': [2], 'encr': ['sha1'], 'auth': ['aes128']}, 'phase2': {'dh': [2], 'encr': ['sha1'], 'auth': ['aes128']}, 'passphrase': 'J5cAf9wGLwjF7KmJadSg_Q2ygz_HDVW8', 'leftSubnets': ['0.0.0.0/0'], 'rightSubnets': ['0.0.0.0/0'], 'ikeLifeTime': '8h', 'lifetime': '1h', 'dpdDelay': '10s', 'dpdTimeout': '30s', 'dpdAction': 'restart', 'type': 'ipsec', 'createdAt': '2021-10-08T16:40:47.522Z', 'updatedAt': '2021-10-12T17:43:48.438Z', 'id': 'DknPxY8JoQ'}], 'createdAt': '2021-10-06T17:02:13.996Z', 'updatedAt': '2021-10-08T16:40:47.528Z', 'id': 'DbVh6dcOb7'}], provider=NetworkProvider(region='br-sao1', continentCode='SA', countryCode='BR'), id='GtgzcTkuH2')], id='ZnpZRW9d9J'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='Liebold Net', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=32.7766642, longitude=-96.7969878), name='Dallas', instances=[{'tenantId': 'knowledgebase', 'network': 'WvNVqlEdNv', 'region': '9rinbCV8dg', 'instanceType': '2048', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-nhdb8end1r.pzero.perimeter81.com', 'ip': '131.226.34.158', 'tunnels': [], 'createdAt': '2021-10-12T20:02:15.639Z', 'updatedAt': '2021-10-15T21:10:54.089Z', 'id': 'NHDB8END1R'}], provider=NetworkProvider(region='sx-ds1', continentCode='NA', countryCode='US'), id='9rinbCV8dg')], id='WvNVqlEdNv'), Network(geoPoint=NetworkGeoPoint(latitude=40.712776, longitude=-74.005974), name='NJ test', isDefault=False, regions=[NetworkRegion(geoPoint=NetworkGeoPoint(latitude=39.833851, longitude=-74.871826), name='New Jersey', instances=[{'tenantId': 'knowledgebase', 'network': 'Ts6c3FMW6K', 'region': 'ic2ZbsAEBA', 'instanceType': '202', 'imageType': 'sxp', 'imageVersion': 'sxp-2021091200', 'resourceId': None, 'dns': 'knowledgebase-wjftj1fodd.pzero.perimeter81.com', 'ip': '149.28.47.96', 'tunnels': [], 'createdAt': '2021-10-18T15:07:55.402Z', 'updatedAt': '2021-10-18T15:07:55.403Z', 'id': 'wjFTj1FoDd'}],
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          provider=NetworkProvider(region='EWR', continentCode='NA', countryCode='US'), id='ic2ZbsAEBA')], id='Ts6c3FMW6K')])
#
