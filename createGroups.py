import requests
import json
import pandas as pd
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--apikey', '-A', type=str, required=True, help='argument takes in the API key from web portal')
parser.add_argument('--file', '-F', type=str, required=True, help='argument takes in an excel format file with groups/descriptions')


args = parser.parse_args()

def pp_json(json_thing, sort=False, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


#First Step is to get the bearer token from the api key. Need to pass it in.
#Should we make it a function?

api_url = "https://api.perimeter81.com/api/v1/auth/authorize"

data = '{"grantType": "api_key", "apiKey": "' + args.apikey + '"}'

#print(data)
#exit()

headers = {'Content-type': 'application/json', 'accept': 'application/json'}

response = requests.post(api_url, headers=headers, data=data)

auth = {}
auth = json.loads(response.text)
#print(auth)
#print(type(auth))

token = auth['data']['accessToken']
#print(token)

bearerToken = {"Authorization": "Bearer " + token}
#print(bearerToken)

#print(auth['data']['accessTokenExpire'])
expires_time = auth['data']['accessTokenExpire']


#datetime_time = datetime.datetime.fromtimestamp(expires_time)
#print(datetime_time)

base_url = 'https://api.perimeter81.com/api/rest'

json_header = {}
json_header['Authorization'] = 'Bearer ' + token
json_header['Accept'] = 'application/json'
json_header['Content-Type'] = 'application/json'
#json_header['Authorization'] = 'accessToken ' + token
#json_header['auth'] = 'Bearer ' + token


xls_file = args.file
data = pd.read_excel (args.file) 
df = pd.DataFrame(data, columns= ['GroupName', 'Description'])
#print(df)
#exit()

def createGroups(base_url, headers):
	url = '/v1/groups'

	#url = '/v1/users?page=1&qType=partial'
	#url = '/v1/users/?page=1&limit=25&q=Ace&qType=full'
	#for name in df_dict['GroupName']:
	for ind in df.index:

		#print(df['GroupName'][ind], df['Description'][ind])
		group_name = df['GroupName'][ind]
		group_desc = df['Description'][ind]
		calldata = '{"name": "' + group_name + '", "description": "' + group_desc + '"}'

		#print(calldata)
		#print(base_url+url)
		#print("###################")
		#print(headers)
		#print("GOT HEADERS")
		print("Creating group " + group_name)
		response = requests.post(base_url+url, headers=headers, data=calldata)
		time.sleep(5)
		print(response.text)

createGroups(base_url, json_header)




