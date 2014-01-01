import json
from websocket import create_connection
ws = create_connection("ws://192.168.0.4:9090/jsonrpc?request=")
print "Sending 'Hello, World'..."
#data = {"jsonrpc":"2.0","id":1,"method":"Playlist.GetPlaylists"}
data = {"jsonrpc":"2.0","id":1,"method":"bob"}
json_data = json.dumps(data)
ws.send(json_data)
result =  ws.recv()
resultj = json.loads(result)
if resultj['error']:
	print resultj['error']
else:
	print "Received '%s'" % resultj
ws.close()
