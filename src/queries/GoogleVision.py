import httplib2
import sys

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

api_key = 'AIzaSyCk4z9TGxyQqz8g3Wy7G23NBem8B32N-J8'

client_id = '1022914954389-5odc0vhkaglul6cglfs1c94loc777scf.apps.googleusercontent.com'
client_key = 'nUpG1IVz6-bEQqCN2ymvpni5'

scope = 'https://console.google.com/apis/vision'

flow = OAuth2WebServerFlow(client_id, client_key, scope)

def main():
	storage = Storage('credentials.dat')
	credentials = storage.get()
	if credentials is None or credentials.invalid:
		credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

	http = httplib2.Http()
	http = credentials.authorize(http)

	service = build('vision', 'v1.3', http=http)

