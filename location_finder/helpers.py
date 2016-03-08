from django.conf import settings
from oauth2client.client import OAuth2WebServerFlow
import requests
import urllib2

import oauth2 as oauth
import time

url = 'https://www.googleapis.com/fusiontables/v2'

params = {
'code': 'INSERT INTO %s (lat, lon, address)'
'VALUES (30, 40, "this is an address";',
  'client_id': client_id,
  'client_secret': client_secret,
  'redirect_uri': redirect_uri,
  'grant_type': 'authorization_code'}



client_id = getattr(settings, "FUSION_TABLES_CLIENT_ID", '')
client_secret = getattr(settings, 'FUSION_TABLES_CLIENT_SECRET', '')


token = oauth.Token(key=client_id, secret=client_secret)
consumer = oauth.Consumer(key=client_id, secret=client_secret)

params['oauth_token'] = token.key
params['oauth_consumer_key'] = consumer.key

req = oauth2.Request(method="PUT", url=url, parameters=params)



settings.configure()



redirect_uri = "http://test.com/oauth2callback"
api_key = "123"
tableid = '1fNXVMeNJr_l31N7ohrGpS91Hge4Q0Pn1fuRCDOf0'

base_url = 'https://www.googleapis.com/fusiontables/v2'


test_data = {'code': 'INSERT INTO %s (lat, lon, address)'
'VALUES (30, 40, "this is an address";',
  'client_id': client_id,
  'client_secret': client_secret,
  'redirect_uri': redirect_uri,
  'grant_type': 'authorization_code'}

print(test_data)
r = requests.post('https://accounts.google.com/o/oauth2/auth',
  data=json.dumps(test_data))
print(r.url)
print(r.status_code)


import httplib2
import oauth2client.appengine
from oauth2client.appengine import AppAssertionCredentials
from apiclient.discovery import build

SCOPE='https://www.googleapis.com/auth/fusiontables'
PROJECT_NUMBER = tableid # REPLACE WITH YOUR Project ID

# Create a new API service for interacting with Fusion Tables
credentials = AppAssertionCredentials(scope=SCOPE)
http = credentials.authorize(httplib2.Http())
logging.info('QQQ: accountname: %s' % app_identity.get_service_account_name())
service = build('fusiontables', 'v1', http=http,
  developerKey='YOUR KEY HERE FROM API CONSOLE')

# Use this oauth:
# http://gspread.readthedocs.org/en/latest/oauth2.html

{
  "iss":"761326798069-r5mljlln1rd4lrbhg75efgigp36m78j5@developer.gserviceaccount.com",
  "scope":"https://www.googleapis.com/auth/devstorage.readonly",
  "aud":"https://www.googleapis.com/oauth2/v4/token",
  "exp":1328554385,
  "iat":1328550785
}

import json
import gspread

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('Finders Keepers-5592a1f8e554.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

#wks = gc.open("Location Table").sheet1
wks = gc.open_by_key('1m_I9W5rWiN6uZbuj0t0s_dEMnJtxh-AGre4Jjp9kFi8').sheet1
# wks.append_row([1,1,'somewhere'])
wks.insert_row([1,1,'somewhere'])

import requests

access_token = credentials.access_token

query = "INSERT INTO 1fNXVMeNJr_l31N7ohrGpS91Hge4Q0Pn1fuRCDOf0 (Latitude, Longitude, Address) VALUES (30, 40, 12);"

data = {'sql': query,
  'key': access_token}
URL = 'https://www.googleapis.com/fusiontables/v1/tables/1fNXVMeNJr_l31N7ohrGpS91Hge4Q0Pn1fuRCDOf0/import'
headers = {
      #'Authorization': 'GoogleLogin auth=' + access_token,
      'Content-Type': 'application/x-www-form-urlencoded',
    }
serv_resp = requests.post(url=URL, data=data, headers=headers)

# troubleshoot token

token_info = 'https://www.googleapis.com/oauth2/v1/tokeninfo'

data_info = {'access_token': access_token}
info = requests.post(url=token_info, data=data_info)
