import os
from _p81api import _api
from _p81api._model import Auth, Group, CreateGroupApiCallResult, ListNetworksApiCallResult, \
    GetNetworksHealthApiCallResult
import unittest


class HelloP81(unittest.TestCase):

    def test_hello(self):
        """
        Not a real test - just kind of hello world
        :return:
        """
        auth: Auth = _api.authenticate(os.getenv('token'))
        group: Group = Group('my_group891zyu', 'my_description')
        result: CreateGroupApiCallResult = _api.create_group(auth, group)
        if result.success:
            print(f'Group was created [or group exists]: {result.results}')
        else:
            print(f'Group was not created: {result.errors[0]}')
        result: ListNetworksApiCallResult = _api.list_networks(auth)
        print(result.success)
        print('-- List of networks & health  --')
        for idx, network in enumerate(result.results, 1):
            print(f'{idx}. {network}')
            health: GetNetworksHealthApiCallResult = _api.get_network_health(auth, network.id)
            for status_lst in health.results:
                for network_status in status_lst:
                    print(f'\t{network_status}. Healthy: {network_status.is_healthy()}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
