import requests
import json


#response = urllib2.urlopen('http://192.168.0.4/jsonrpc?request=')
def send_request(move):
	url = 'http://192.168.0.4:10000/jsonrpc?request='
	headers = {'Content-Type' : 'Contentapplication/json', 'User-Agent' : 'rhys-xbmc-remote'}
	data = {'jsonrpc':'2.0','id': 1}
	data['method'] = 'Input.'+move
	data_json = json.dumps(data)
	#print url+data_json
	r = requests.get(url+data_json, headers=headers)
	#print r.content
	#print r.headers
	if r.status_code != 200:
		return('There has been some kind of issue. Status = '+r.status_code)

def test():
	baseurl = 'http://192.168.0.4:10000/jsonrpc?request='
	headers = {'Content-Type' : 'application/json', 'User-Agent' : 'rhys-xbmc-remote'}
	data = {'jsonrpc':'2.0','id': 1}
	data['method'] = 'Input.Down'
	data_json = json.dumps(data)
	url = baseurl+data_json
	print url
	r = requests.get(url, headers=headers)
	print r.content
	print r.headers
	print r.status_code

if __name__ == '__main__':
	test()