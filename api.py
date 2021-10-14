import http.client
import json
import urllib.request
from copy import copy
from dataclasses import asdict
from typing import List, Dict

from model import (
    Group,
    Err,
    Auth,
    CreateGroupResponse,
    User,
    CreateUserResponse,
    CreateGroupApiCallResult,
    CreateUserApiCallResult,
    ApiCallResultBase, ListUsersArguments
)

_AUTH_URL = 'https://api.perimeter81.com/api/v1/auth/authorize'
_BASE_URL = 'https://api.perimeter81.com/api/rest'
_AUTH_HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json',
                 'Authorization': '<REPLACE_ME>'}


def create_user(auth: Auth, user: User) -> CreateUserApiCallResult:
    return create_users(auth, [user])


def create_users(auth: Auth, users: List[User]) -> CreateUserApiCallResult:
    url: str = f'{_BASE_URL}/v1/users'
    errors: List[Err] = []
    results: List[CreateUserResponse] = []
    for user in users:
        payload = asdict(user)
        try:
            response: Dict = _post(url, auth, payload, 201)
            results.append(CreateUserResponse(**response))
        except Exception as e:
            errors.append(str(e))
    return CreateUserApiCallResult(len(errors) == 0, errors, results)


def delete_user(auth: Auth, user_id: str) -> ApiCallResultBase:
    return delete_users(auth, [user_id])


def delete_users(auth: Auth, user_ids: List[str]) -> ApiCallResultBase:
    url_template: str = '{}/v1/users/{}'
    errors: List[Err] = []
    for user_id in user_ids:
        url: str = url_template.format(_BASE_URL, user_id)
        try:
            _delete(url, auth)
        except Exception as e:
            errors.append(str(e))
    return ApiCallResultBase(len(errors) == 0, errors)


def list_users(auth: Auth, list_users_args: ListUsersArguments):
    #url: str = f'{_BASE_URL}/v1/users/'
    #url =
    # TODO waiting for input from David 
    pass


def create_group(auth: Auth, group: Group) -> CreateGroupApiCallResult:
    return create_groups(auth, [group])


def create_groups(auth: Auth, groups: List[Group]) -> CreateGroupApiCallResult:
    url: str = f'{_BASE_URL}/v1/groups'
    errors: List[Err] = []
    results: List[CreateGroupResponse] = []
    for group in groups:
        payload = asdict(group)
        try:
            response: Dict = _post(url, auth, payload, 201)
            results.append(CreateGroupResponse(**response))
        except Exception as e:
            errors.append(str(e))
    return CreateGroupApiCallResult(len(errors) == 0, errors, results)


def delete_group(auth: Auth, group_id: str) -> ApiCallResultBase:
    return delete_groups(auth, [group_id])


def delete_groups(auth: Auth, group_ids: List[str]) -> ApiCallResultBase:
    url_template: str = '{}/v1/groups/{}'
    errors: List[Err] = []
    for group_id in group_ids:
        url: str = url_template.format(_BASE_URL, group_id)
        try:
            _delete(url, auth)
        except Exception as e:
            errors.append(str(e))
    return ApiCallResultBase(len(errors) == 0, errors)


def authenticate(api_key: str) -> Auth:
    def _make_headers(token: str) -> Auth:
        result: Dict = copy(_AUTH_HEADERS)
        result['Authorization'] = f'Bearer {token}'
        return result

    data: Dict = {'grantType': 'api_key', 'apiKey': api_key}
    headers: Dict = {'Content-type': 'application/json', 'accept': 'application/json'}
    auth: Dict = _post(_AUTH_URL, headers, data)
    return _make_headers(auth['data']['accessToken'])


def _delete(url: str, headers: Dict, expected_status_code: int = 200) -> None:
    request: urllib.request.Request = urllib.request.Request(url=url, method='DELETE', headers=headers)
    response: http.client.HTTPResponse = urllib.request.urlopen(request)
    if response.getcode() != expected_status_code:
        reason: str = response.read()
        raise Exception(
            f'Expected status code: {expected_status_code}. Actual status code: {response.getcode()}. Reason: {reason}')


def _post(url: str, headers: Dict, payload: Dict, expected_status_code: int = 200) -> Dict:
    params: str = json.dumps(payload).encode('utf8')
    request: urllib.request.Request = urllib.request.Request(url, data=params, headers=headers)
    response: http.client.HTTPResponse = urllib.request.urlopen(request)
    if response.getcode() != expected_status_code:
        reason: str = response.read()
        raise Exception(
            f'Expected status code: {expected_status_code}. Actual status code: {response.getcode()}. Reason: {reason}')
    else:
        return json.loads(response.read().decode('utf8'))
