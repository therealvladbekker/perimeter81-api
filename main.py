import argparse
from csv import reader
from typing import List
import logging
import api
from model import Group, Auth, CreateGroupResponse, ApiCallResultBase, CreateGroupApiCallResult, \
    ListNetworksApiCallResult


def main():
    def _get_groups(file_name: str) -> List[Group]:
        results: List[Group] = []
        with open(file_name, 'r') as f:
            csv_reader = reader(f)
            header = next(csv_reader)
            if header is not None:
                for row in csv_reader:
                    results.append(Group(*row))
        return results

    parser = argparse.ArgumentParser()
    parser.add_argument('--apikey', '-A', type=str, required=True, help='argument takes in the API key from web portal')
    parser.add_argument('--file', '-F', type=str, required=True,
                        help='argument takes in a csv format file with groups/descriptions')
    args = parser.parse_args()
    groups: List[Group] =  [] #_get_groups(args.file)
    auth: Auth = api.authenticate(args.apikey)
    networks: ListNetworksApiCallResult = api.list_networks(auth)
    if networks.success:
        for nw in networks.results:
            print(nw.id)
            print(api.get_network_health(auth,nw.id))
    # result: CreateGroupApiCallResult = api.create_groups(auth, groups)
    # if not result.success:
    #     logging.error(f'Failed to create {len(result.errors)} groups. Details: {result.errors}')
    # else:
    #     print(f'{len(groups)} groups were created. Details below:')
    #     create_group_response: CreateGroupResponse
    #     for idx, create_group_response in enumerate(result.data, 1):
    #         print(f'{idx}) {create_group_response}')
    #         delete_result: ApiCallResultBase = api.delete_group(auth, create_group_response.id)
    #         if not delete_result.success:
    #             logging.error(f'Failed to delete group {create_group_response.id}')
    #         else:
    #             print(f'Group {create_group_response.id} was deleted')


if __name__ == "__main__":
    main()
