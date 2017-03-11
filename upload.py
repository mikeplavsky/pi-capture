from oauth2client import client
from apiclient import discovery
from apiclient.http import MediaFileUpload 
import httplib2

token = ''

with open("./tokens.json") as f:
    tokens = f.read()

creds = client.OAuth2Credentials.from_json(tokens)
creds.refresh(httplib2.Http())

http_auth = creds.authorize(httplib2.Http())

drive = discovery.build('drive','v3', http=http_auth)
res = drive.files().list(q="name = 'Camera'").execute()

for f in res.get('files',[]):
    print(f.get('name'), f.get('id'))

import sys, os

img = sys.argv[1]
img_name = os.path.basename(img)

file_metadata = dict(
        name=img_name,
        parents=[f.get('id')])

media = MediaFileUpload(
        img,
        mimetype="image/jpg",
        resumable=True)

res = drive.files().create(
        body=file_metadata,
        media_body=media,
        fields='id').execute()

print("File ID: %s" % res.get('id'))

